"""wiki 全体と ToDo リストを Markdown でファイルに書き出す．人間が中身を確かめるためのコマンド．

    uv run defwiki-export [--out-dir DIR]

DIR（既定: exports）に wiki.md と todo.md を書き出す．参照はページ内リンクにする．
定義は用語，識別子の順に，ToDo は上から順に並べる．todo.md の参照は wiki.md の定義へリンクし，
wiki.md の各定義の末尾には，その定義を参照する ToDo へのリンクを並べる．
データベースは環境変数 DEFWIKI_DB が指す場所，なければ ~/.defwiki/wiki.db．書き換えない．
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from .wiki import Wiki, _replace_refs, _scan, default_db

WIKI_FILE = "wiki.md"
TODO_FILE = "todo.md"

_LINK_TEXT_SPECIAL = re.compile(r"([\\\[\]])")


def _md_link(id: str, term: str, page: str = "") -> str:
    text = _LINK_TEXT_SPECIAL.sub(r"\\\1", term)
    return f"[{text}]({page}#{id})"


def _md_refs(text: str, page: str = "") -> str:
    """提示形式の参照を `[用語](page#識別子)` に置換える．"""
    refs, _, _ = _scan(text, stored=False)
    return _replace_refs(text, refs, lambda r: _md_link(r.id, r.term, page))[0]


def _todo_backrefs(wiki: Wiki) -> dict[str, list[int]]:
    """識別子ごとに，それを参照する ToDo の番号を上から順に並べる．"""
    back: dict[str, list[int]] = {}
    for t in wiki.todos():
        refs, _, _ = _scan(t["text"], stored=False)
        for id in dict.fromkeys(r.id for r in refs):
            back.setdefault(id, []).append(t["id"])
    return back


def wiki_markdown(wiki: Wiki) -> str:
    """提示形式を変換する．定義ごとに，識別子を id とする見えないアンカーと `## 用語` の見出しを置き，参照を `[用語](#識別子)` で表す．

    定義を参照する ToDo があれば，末尾に `ToDo: [番号](todo.md#todo-番号)，…` の行を置く．
    """
    back = _todo_backrefs(wiki)
    blocks = []
    for id in wiki.ids():
        head, _, desc = wiki.get([id]).partition("\n")
        term = head[len(f"# [[{id}]] "):]
        paras = [f'<a id="{id}"></a>', f"## {term}"]
        if desc:
            paras.append(_md_refs(desc))
        if id in back:
            paras.append("ToDo: " + "，".join(f"[{n}]({TODO_FILE}#todo-{n})" for n in back[id]))
        blocks.append("\n\n".join(paras))
    return "\n\n".join(blocks) + "\n" if blocks else ""


def todo_markdown(wiki: Wiki) -> str:
    """ToDo ごとに `todo-番号` を id とする見えないアンカーと `## 番号` の見出しと本文を置き，参照を `[用語](wiki.md#識別子)` で表す．"""
    blocks = [
        f'<a id="todo-{t["id"]}"></a>\n\n## {t["id"]}\n\n{_md_refs(t["text"], WIKI_FILE)}' for t in wiki.todos()
    ]
    return "\n\n".join(blocks) + "\n" if blocks else ""


def export(wiki: Wiki, out_dir: Path) -> None:
    """out_dir に wiki.md と todo.md を書き出す．out_dir がなければ作る．"""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / WIKI_FILE).write_text(wiki_markdown(wiki), encoding="utf-8")
    (out_dir / TODO_FILE).write_text(todo_markdown(wiki), encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(prog="defwiki-export", description="wiki 全体と ToDo リストを書き出す．")
    p.add_argument("--out-dir", default="exports", help=f"{WIKI_FILE} と {TODO_FILE} の書き出し先（既定: exports）")
    args = p.parse_args()
    db = default_db()
    if not db.exists():
        sys.exit(f"データベースがない: {db}")
    wiki = Wiki(db)
    try:
        export(wiki, Path(args.out_dir).expanduser())
    finally:
        wiki.close()


if __name__ == "__main__":
    main()
