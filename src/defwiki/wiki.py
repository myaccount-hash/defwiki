"""defwiki の保持と検証．

説明と ToDo の本文の中の参照は `[[識別子]]` として保存し，提示時に `[[識別子|用語]]` へ戻す．
`create` の入力では，同じ呼び出しで作る定義を `[[$仮名|用語]]` で参照できる．
"""

from __future__ import annotations

import os
import re
import secrets
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

ID_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789"
ID_LEN = 6
_ID = rf"[a-z0-9]{{{ID_LEN}}}"
_KEY = r"[a-z0-9_]+"
KEY_RE = re.compile(rf"^{_KEY}$")
_INPUT_REF_HEAD = re.compile(rf"\[\[({_ID}|\${_KEY})\|")
_STORED_REF = re.compile(rf"\[\[({_ID})\]\]")
_TICKS = re.compile(r"`+")
_EXTERNAL = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*://\S+")
EXCERPT_LEN = 80
EXCERPT_BEFORE = 20

_SCHEMA = """
CREATE TABLE IF NOT EXISTS defs (
    id TEXT PRIMARY KEY,
    term TEXT NOT NULL,
    description TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS refs (
    src TEXT NOT NULL,
    dst TEXT NOT NULL,
    PRIMARY KEY (src, dst)
);
CREATE INDEX IF NOT EXISTS refs_dst ON refs (dst);
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    pos INTEGER NOT NULL
);
"""


def default_db() -> Path:
    """環境変数 DEFWIKI_DB が指す場所．なければ ~/.defwiki/wiki.db．"""
    return Path(os.environ.get("DEFWIKI_DB", "~/.defwiki/wiki.db")).expanduser()


class WikiError(Exception):
    """書込みの拒否や不正な要求．メッセージはそのままLLMに返す．"""

    def __init__(self, errors: list[str] | str):
        self.errors = [errors] if isinstance(errors, str) else errors
        super().__init__("\n".join(self.errors))


@dataclass(frozen=True)
class Ref:
    id: str  # 入力では`$仮名`でもよい
    term: str  # 入力では書かれた用語，保存形式では空
    start: int
    end: int


# ---------------------------------------------------------------- 字句処理


def term_errors(term: str) -> list[str]:
    errs = []
    if term == "":
        errs.append("用語が空である．")
        return errs
    if "\n" in term or "\r" in term:
        errs.append("用語が複数行である．")
    if term != term.strip():
        errs.append("用語の前後に空白がある．")
    if "[[" in term or "]]" in term:
        errs.append("用語が`[[`または`]]`を含む．")
    if term.endswith("]"):
        errs.append("用語が`]`で終わる．")
    if "`" in term:
        errs.append("用語がバッククォートを含む．")
    return errs


def normalize_description(text: str) -> str:
    """改行を LF に揃え，前後の空行を除く．"""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return "\n".join(lines)


def _code_end(text: str, m: re.Match) -> int | None:
    """バッククォートの連続 m が開くコードスパンの終端．閉じる同じ長さの連続がなければ None．"""
    n = m.end() - m.start()
    for c in _TICKS.finditer(text, m.end()):
        if c.end() - c.start() == n:
            return c.end()
    return None


def _scan(text: str, stored: bool) -> tuple[list[Ref], list[tuple[int, int]], list[str]]:
    """参照とコードスパンを左から順に取り出す．コードスパン内の `[[` は参照の開始ではない．"""
    refs: list[Ref] = []
    codes: list[tuple[int, int]] = []
    errs: list[str] = []
    i, n = 0, len(text)
    while i < n:
        if m := _TICKS.match(text, i):
            end = _code_end(text, m)
            if end is not None:
                codes.append((i, end))
            i = end or m.end()
            continue
        if not text.startswith("[[", i):
            i += 1
            continue
        if stored:
            m = _STORED_REF.match(text, i)
            if not m:  # 保存形式は本モジュールが書くので起こらない
                raise RuntimeError(f"保存形式が壊れている: {text!r}")
            refs.append(Ref(m.group(1), "", i, m.end()))
            i = m.end()
            continue
        m = _INPUT_REF_HEAD.match(text, i)
        j = text.find("]]", m.end()) if m else -1
        if not m or j == -1:
            snippet = text[i : i + 20].split("\n")[0].replace("`", "")
            errs.append(
                f"`{snippet}`: `[[`は参照の開始だが`[[識別子|用語]]`または`[[$仮名|用語]]`の形でない．"
                "参照でない`[[`はコードスパンの中に書く．"
            )
            i += 2
            continue
        refs.append(Ref(m.group(1), text[m.end() : j], i, j + 2))
        i = j + 2
    return refs, codes, errs


def _replace_refs(text: str, refs: list[Ref], fmt) -> tuple[str, list[tuple[int, int]]]:
    """参照を fmt の結果に置き換える．置き換えた後の文字列と，その中での各参照の範囲を返す．"""
    out, spans, pos, length = [], [], 0, 0
    for r in refs:
        chunk, ref = text[pos : r.start], fmt(r)
        out += [chunk, ref]
        length += len(chunk)
        spans.append((length, length + len(ref)))
        length += len(ref)
        pos = r.end
    out.append(text[pos:])
    return "".join(out), spans


def _link(id: str, term: str) -> str:
    return f"[[{id}|{term}]]"


def _readable(stored: str) -> bool:
    try:
        _scan(stored, stored=True)
    except RuntimeError:
        return False
    return True


def _substitute(stored: str, id: str, to: str) -> str:
    """保存形式の中の id への参照を to に置き換える．

    to が参照でなく，前後の `[` と合わさって `[[` をなす場合は，to をコードスパンにする．
    """
    refs = [r for r in _scan(stored, stored=True)[0] if r.id == id]
    out, _ = _replace_refs(stored, refs, lambda r: to)
    if not _readable(out):
        out, _ = _replace_refs(stored, refs, lambda r: f"`{to}`")
    return out


def _excerpt(text: str, ref_spans: list[tuple[int, int]], at: int = 0, length: int = 0) -> str:
    """text の at から length 文字の一致を含む抜粋．既定では先頭から切る．

    一致の EXCERPT_BEFORE 文字前から EXCERPT_LEN 文字を取り，一致が収まらなければ一致の終わりまで延ばす．
    参照の途中にかかる端は，参照の端まで広げる．切った側には `…` を付ける．
    """
    start = max(0, at - EXCERPT_BEFORE)
    end = min(len(text), max(start + EXCERPT_LEN, at + length))
    for s, e in ref_spans:
        if s < start < e:
            start = s
        if s < end < e:
            end = e
    return ("…" if start > 0 else "") + text[start:end] + ("…" if end < len(text) else "")


def _apply_edits(text: str, edits: list[dict]) -> str:
    """edits の old を new に先頭から順に置き換える．old はその時点の text にちょうど1回現れる．"""
    errs = []
    for i, e in enumerate(edits):
        n = text.count(e["old"])
        if n == 1:
            text = text.replace(e["old"], e["new"])
        elif n == 0:
            errs.append(f"edits[{i}]: `old`が説明に現れない．")
        else:
            errs.append(f"edits[{i}]: `old`が説明に{n}回現れる．一意に定まるよう前後を含める．")
    if errs:
        raise WikiError(errs)
    return text


def _own_length(stored: str) -> int:
    """説明の長さ．参照は0文字と数える．"""
    refs, _, _ = _scan(stored, stored=True)
    return len(stored) - sum(r.end - r.start for r in refs)


def _char_class(c: str) -> str | None:
    """語の境界の判定に用いる文字の種別．英数字とカタカナ以外は None．"""
    if c.isascii() and (c.isalnum() or c == "_"):
        return "ascii"
    if "\u30a1" <= c <= "\u30fa" or c in "ーヽヾ":
        return "katakana"
    return None


def _same_class(a: str, b: str) -> bool:
    return _char_class(a) is not None and _char_class(a) == _char_class(b)


def _plain_terms(stored: str, index: dict[str, list[str]]) -> list[str]:
    """参照とコードスパンの外側に現れる用語を，最長一致で左から順に取り出す．

    先頭または末尾が英数字またはカタカナの用語は，同じ種別の文字に隣接する位置では一致としない．
    一致としなかった箇所は，より短い用語を探さずに読み飛ばす．
    """
    refs, codes, _ = _scan(stored, stored=True)
    found: dict[str, None] = {}
    skips = sorted([(r.start, r.end) for r in refs] + codes)
    bounds = [0] + [x for span in skips for x in span] + [len(stored)]
    for start, end in zip(bounds[::2], bounds[1::2]):
        seg = stored[start:end]
        i = 0
        while i < len(seg):
            for term in index.get(seg[i], ()):
                j = i + len(term)
                if not seg.startswith(term, i):
                    continue
                if not (i > 0 and _same_class(term[0], seg[i - 1])
                        or j < len(seg) and _same_class(term[-1], seg[j])):
                    found[term] = None
                i = j
                break
            else:
                i += 1
    return list(found)


# ---------------------------------------------------------------- 点検


def _groups(rows, col: int) -> list[list[str]]:
    """col 列が同じで空でない定義の組．"""
    groups: dict[str, list[str]] = {}
    for r in rows:
        if r[col]:
            groups.setdefault(r[col], []).append(r[0])
    return [g for g in groups.values() if len(g) > 1]


def _unlinked(rows) -> dict[str, list[str]]:
    """定義ごとに，説明に参照なしで現れる用語を持つ他の定義．"""
    by_term: dict[str, list[str]] = {}
    for id, term, _ in rows:
        by_term.setdefault(term, []).append(id)
    index: dict[str, list[str]] = {}
    for term in sorted(by_term, key=len, reverse=True):
        index.setdefault(term[0], []).append(term)
    out = {}
    for id, _, stored in rows:
        ids = [i for t in _plain_terms(stored, index) for i in by_term[t] if i != id]
        if ids:
            out[id] = ids
    return out


class _Audit:
    """ある時点の wiki 全体についての，運用規則への違反の疑い．"""

    def __init__(self, rows: list[tuple[str, str, str]], isolated: list[str]):
        self.terms = {id: term for id, term, _ in rows}
        self.isolated = isolated
        self.same_descriptions = _groups(rows, 2)
        self.unlinked = _unlinked(rows)
        self.external = {id: m.group() for id, _, stored in rows if (m := _EXTERNAL.search(stored))}

    def _listed(self, ids) -> str:
        return ", ".join(_link(i, self.terms[i]) for i in ids)

    def report(self, limit: int = 20) -> dict:
        """項目ごとに limit 件と，項目ごとの全件数．"""

        def d(id):
            return {"id": id, "term": self.terms[id]}

        items = {
            "isolated": [d(i) for i in self.isolated],
            "duplicate_descriptions": [[d(i) for i in g] for g in self.same_descriptions],
            "unlinked": [{**d(i), "mentions": [d(m) for m in ms]} for i, ms in self.unlinked.items()],
            "external": [d(i) for i in self.external],
        }
        return {**{k: v[:limit] for k, v in items.items()}, "counts": {k: len(v) for k, v in items.items()}}

    def warnings(self, id: str, term_changed: bool, description_changed: bool, created: bool = False) -> list[str]:
        """書き込んだ定義についての疑いを返す．

        作った定義には，参照も被参照もないことを警告しない．書いた時点で自明だからである．
        """

        def others(groups):
            return [i for g in groups if id in g for i in g if i != id]

        out = []
        if term_changed:
            if srcs := [i for i, ms in self.unlinked.items() if id in ms]:
                out.append(f"この用語が参照なしで現れる定義がある: {self._listed(srcs)}")
        if description_changed:
            if id in self.isolated and not created:
                out.append("参照も被参照もない．")
            if id in self.unlinked:
                out.append(f"既存の定義の用語が参照なしで現れる: {self._listed(self.unlinked[id])}")
            if same := others(self.same_descriptions):
                out.append(f"説明が同一の定義がある: {self._listed(same)}")
            if id in self.external:
                out.append(f"外部への参照を含む: `{self.external[id]}`")
        return out


# ---------------------------------------------------------------- wiki


class Wiki:
    def __init__(self, path: str | Path):
        self.db = sqlite3.connect(str(path), isolation_level=None, check_same_thread=False)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA busy_timeout=5000")
        self.db.executescript(_SCHEMA)
        self._migrate()

    def close(self) -> None:
        self.db.close()

    # ---- 内部

    def _migrate(self) -> None:
        """版0の ToDo は本文を提示形式のまま持ち，参照を検証していない．保存形式に直す．

        識別子と用語が現在の定義と一致する参照だけを参照として残し，他は用語の文字列にする．
        """

        def version():
            return self.db.execute("PRAGMA user_version").fetchone()[0]

        if version() >= 1:
            return
        with self._tx():
            if version() >= 1:  # 他のプロセスが先に直した
                return
            for n, text in self.db.execute("SELECT id, text FROM todos").fetchall():
                refs, _, _ = _scan(text, stored=False)
                terms = self._terms(r.id for r in refs)
                stored, _ = _replace_refs(
                    text, refs, lambda r: f"[[{r.id}]]" if terms.get(r.id) == r.term else r.term
                )
                if not _readable(stored):  # 参照の形でない`[[`がある
                    stored = _replace_refs(text, refs, lambda r: r.term)[0].replace("[[", "[ [")
                self.db.execute("UPDATE todos SET text=? WHERE id=?", (stored, n))
            self.db.execute("PRAGMA user_version = 1")

    def _rows(self) -> list[tuple[str, str, str]]:
        return self.db.execute("SELECT id, term, description FROM defs ORDER BY term, id").fetchall()

    def _terms(self, ids) -> dict[str, str]:
        ids = list(set(ids))
        if not ids:
            return {}
        q = ",".join("?" * len(ids))
        return dict(self.db.execute(f"SELECT id, term FROM defs WHERE id IN ({q})", ids))

    def _exists(self, id: str) -> bool:
        return self.db.execute("SELECT 1 FROM defs WHERE id=?", (id,)).fetchone() is not None

    def _require(self, id: str) -> None:
        if not self._exists(id):
            raise WikiError(f"識別子`{id}`の定義は存在しない．")

    def _render(self, stored: str, terms: dict[str, str] | None = None) -> tuple[str, list[tuple[int, int]]]:
        """保存形式を提示形式に戻す．提示形式と，その中での各参照の範囲を返す．"""
        refs, _, _ = _scan(stored, stored=True)
        if terms is None:
            terms = self._terms(r.id for r in refs)
        return _replace_refs(stored, refs, lambda r: _link(r.id, terms[r.id]))

    def _parse_input(self, description: str, keys: dict[str, str] | None = None) -> tuple[str, set[str]]:
        """説明を検証し，保存形式と参照先の集合を返す．違反があれば WikiError．

        keys は仮名から識別子への対応．`[[$仮名|用語]]` はこれで解決する．
        """
        text = normalize_description(description)
        refs, _, errs = _scan(text, stored=False)
        ids = {r.id: (keys or {}).get(r.id[1:]) if r.id.startswith("$") else r.id for r in refs}
        terms = self._terms(i for i in ids.values() if i)
        for r in refs:
            id = ids[r.id]
            if id is None:
                errs.append(f"`{_link(r.id, r.term)}`: 仮名`{r.id}`の定義はこの呼び出しにない．")
            elif id not in terms:
                errs.append(f"`{_link(r.id, r.term)}`: 識別子`{r.id}`の定義は存在しない．")
            elif r.term != terms[id]:
                errs.append(
                    f"`{_link(r.id, r.term)}`: 用語が参照先の現在の用語と一致しない．"
                    f"現在の用語は`{terms[id]}`．"
                )
        if errs:
            raise WikiError(errs)
        stored, _ = _replace_refs(text, refs, lambda r: f"[[{ids[r.id]}]]")
        return stored, {ids[r.id] for r in refs}

    def _new_id(self) -> str:
        while True:
            id = "".join(secrets.choice(ID_CHARS) for _ in range(ID_LEN))
            if not self._exists(id):
                return id

    @contextmanager
    def _tx(self, commit: bool = True):
        """書込みのトランザクション．例外で抜けるか，commit が偽であれば取り消す．"""
        self.db.execute("BEGIN IMMEDIATE")
        try:
            yield
        except BaseException:
            self.db.execute("ROLLBACK")
            raise
        self.db.execute("COMMIT" if commit else "ROLLBACK")

    def _set_description(self, id: str, stored: str, dsts: set[str]) -> None:
        self.db.execute("UPDATE defs SET description=? WHERE id=?", (stored, id))
        self.db.execute("DELETE FROM refs WHERE src=?", (id,))
        self.db.executemany("INSERT INTO refs (src, dst) VALUES (?, ?)", [(id, d) for d in dsts])

    def _isolated(self) -> list[str]:
        """自己参照を除いて，参照も被参照もない定義．"""
        rows = self.db.execute(
            "SELECT id FROM defs d WHERE NOT EXISTS "
            "(SELECT 1 FROM refs r WHERE r.src != r.dst AND (r.src = d.id OR r.dst = d.id)) "
            "ORDER BY term, id"
        )
        return [r[0] for r in rows]

    def _remove(self, id: str) -> None:
        self.db.execute("DELETE FROM refs WHERE src=?", (id,))
        self.db.execute("DELETE FROM defs WHERE id=?", (id,))

    def _retarget_todos(self, id: str, to: str) -> None:
        """ToDo の本文にある id への参照を to に置き換える．"""
        rows = self.db.execute("SELECT id, text FROM todos WHERE instr(text, ?)", (f"[[{id}]]",)).fetchall()
        for n, stored in rows:
            self.db.execute("UPDATE todos SET text=? WHERE id=?", (_substitute(stored, id, to), n))

    def _newly_isolated(self, before: set[str]) -> list[str]:
        """before になかった，参照も被参照もない定義についての警告．"""
        left = [i for i in self._isolated() if i not in before]
        if not left:
            return []
        terms = self._terms(left)
        return ["参照も被参照もなくなった定義がある: " + ", ".join(_link(i, terms[i]) for i in left)]

    def _audit(self) -> _Audit:
        return _Audit(self._rows(), self._isolated())

    # ---- ツール

    def ids(self) -> list[str]:
        """全ての定義の識別子．用語，識別子の順．"""
        return [r[0] for r in self._rows()]

    def check(self, limit: int = 20) -> dict:
        return self._audit().report(limit)

    def get(self, ids: list[str]) -> str:
        q = ",".join("?" * len(ids))
        rows = {r[0]: r for r in self.db.execute(f"SELECT id, term, description FROM defs WHERE id IN ({q})", ids)}
        missing = [i for i in ids if i not in rows]
        if missing:
            raise WikiError(f"存在しない識別子: {', '.join(missing)}")
        blocks = []
        for i in ids:
            _, term, stored = rows[i]
            desc, _ = self._render(stored)
            blocks.append(f"# [[{i}]] {term}" + (f"\n{desc}" if desc else ""))
        return "\n\n".join(blocks)

    def search(self, queries: list[str], limit: int = 10) -> dict:
        """文字列ごとに探す．limit は文字列ごとの上限．"""
        rows = self._rows()
        terms = {r[0]: r[1] for r in rows}
        shown = [(id, term, *self._render(stored, terms)) for id, term, stored in rows]
        results = []
        for query in queries:
            hits = []
            for id, term, desc, spans in shown:
                if query in term or query in desc:
                    rank = 0 if term == query else 1 if query in term else 2
                    hits.append((rank, term, id, desc, spans))
            hits.sort(key=lambda h: h[:3])
            results.append({
                "query": query,
                "hits": [
                    {
                        "id": id,
                        "term": term,
                        "excerpt": _excerpt(desc, spans, *((desc.find(query), len(query)) if rank == 2 else ())),
                    }
                    for rank, term, id, desc, spans in hits[:limit]
                ],
                "truncated": len(hits) > limit,
            })
        return {"results": results}

    def longest(self, limit: int = 20, with_description: bool = False) -> dict:
        """説明の長い順に limit 件．長さが同じなら用語，識別子の順．

        with_description が真なら，提示形式の説明も返す．
        """
        rows = [(-_own_length(stored), term, id, stored) for id, term, stored in self._rows()]
        rows.sort()
        defs = []
        for n, term, id, stored in rows[:limit]:
            d = {"id": id, "term": term, "length": -n}
            if with_description:
                d["description"] = self._render(stored)[0]
            defs.append(d)
        return {"defs": defs, "truncated": len(rows) > limit}

    def references(self, id: str, limit: int = 20) -> dict:
        """用語，識別子の順に limit 件．"""
        self._require(id)
        rows = self.db.execute(
            "SELECT d.id, d.term FROM refs r JOIN defs d ON d.id = r.src WHERE r.dst=? ORDER BY d.term, d.id LIMIT ?",
            (id, limit + 1),
        ).fetchall()
        return {"referrers": [{"id": i, "term": t} for i, t in rows[:limit]], "truncated": len(rows) > limit}

    def create(self, defs: list[dict], dry_run: bool = False) -> dict:
        """定義をまとめて作成する．1件でも違反があれば，どれも作成しない．

        警告は，全件を作成した後の状態について返す．
        dry_run が真であれば，作成せずに警告だけを返す．識別子は残らないので，
        警告の中では，この呼び出しの定義を `[[識別子|用語]]` でなく defs の中の位置と用語で示す．
        """

        def name(i):
            return f"defs[{i}] `{defs[i]['term']}`"

        def label(i):
            return name(i) + ": "

        errs = []
        keys: dict[str, str] = {}  # 仮名から識別子へ．識別子は作成時に埋める
        for i, d in enumerate(defs):
            errs += [label(i) + e for e in term_errors(d["term"])]
            if (key := d.get("key")) is None:
                continue
            if not KEY_RE.match(key):
                errs.append(label(i) + f"仮名`{key}`が`[a-z0-9_]`の1文字以上でない．")
            elif key in keys:
                errs.append(label(i) + f"仮名`{key}`が重複している．")
            else:
                keys[key] = ""
        if errs:
            raise WikiError(errs)
        with self._tx(commit=not dry_run):
            # 循環参照を解決できるよう，説明を検証する前に全件の識別子を割り当てる
            ids = []
            for d in defs:
                ids.append(id := self._new_id())
                self.db.execute("INSERT INTO defs (id, term, description) VALUES (?, ?, '')", (id, d["term"]))
                if "key" in d:
                    keys[d["key"]] = id
            for i, (id, d) in enumerate(zip(ids, defs)):
                try:
                    self._set_description(id, *self._parse_input(d["description"], keys))
                except WikiError as e:
                    errs += [label(i) + m for m in e.errors]
            if errs:
                raise WikiError(errs)
            audit = self._audit()
            warnings = [
                f"{_link(id, d['term'])}: {w}"
                for id, d in zip(ids, defs)
                for w in audit.warnings(id, True, True, created=True)
            ]
            if dry_run:
                for i, (id, d) in enumerate(zip(ids, defs)):
                    warnings = [w.replace(_link(id, d["term"]), name(i)) for w in warnings]
                return {"warnings": warnings}
            created = [
                {"id": id, "term": d["term"], **({"key": d["key"]} if "key" in d else {})}
                for id, d in zip(ids, defs)
            ]
            return {"defs": created, "warnings": warnings}

    def update(self, id: str, description: str | None = None, edits: list[dict] | None = None) -> list[str]:
        """説明を description で置き換えるか，提示形式の説明に edits の置換を順に施す．"""
        if (description is None) == (edits is None):
            raise WikiError("`description`と`edits`のどちらか一方だけを渡す．")
        with self._tx():
            self._require(id)
            if edits is not None:
                (stored,) = self.db.execute("SELECT description FROM defs WHERE id=?", (id,)).fetchone()
                description = _apply_edits(self._render(stored)[0], edits)
            self._set_description(id, *self._parse_input(description))
            return self._audit().warnings(id, False, True)

    def rename(self, id: str, term: str) -> list[str]:
        with self._tx():
            self._require(id)
            if errs := term_errors(term):
                raise WikiError(errs)
            self.db.execute("UPDATE defs SET term=? WHERE id=?", (term, id))
            return self._audit().warnings(id, True, False)

    def delete(self, id: str) -> list[str]:
        with self._tx():
            self._require(id)
            others = [r for r in self.references(id)["referrers"] if r["id"] != id]
            if others:
                listed = ", ".join(_link(r["id"], r["term"]) for r in others)
                raise WikiError(f"参照されている定義は削除できない．参照元: {listed}")
            before = set(self._isolated())
            self._retarget_todos(id, self._terms([id])[id])
            self._remove(id)
            return self._newly_isolated(before)

    def merge(self, id: str, into: str) -> list[str]:
        """id への参照を全て into への参照に置き換え，id を削除する．

        警告は，統合した後の状態について返す．
        """
        with self._tx():
            self._require(id)
            self._require(into)
            if id == into:
                raise WikiError("定義をそれ自身に統合することはできない．")
            before = set(self._isolated())
            srcs = [r["id"] for r in self.references(id)["referrers"] if r["id"] != id]
            for src in srcs:
                (stored,) = self.db.execute("SELECT description FROM defs WHERE id=?", (src,)).fetchone()
                refs, _, _ = _scan(stored, stored=True)
                dsts = {into if r.id == id else r.id for r in refs}
                stored, _ = _replace_refs(stored, refs, lambda r: f"[[{into if r.id == id else r.id}]]")
                self._set_description(src, stored, dsts)
            self._retarget_todos(id, f"[[{into}]]")
            self._remove(id)
            audit = self._audit()
            warnings = [f"{_link(s, audit.terms[s])}: {w}" for s in srcs for w in audit.warnings(s, False, True)]
            return warnings + self._newly_isolated(before | set(srcs))

    # ---- ToDo．本文は参照を含んでよい．ToDo からの参照は，被参照に数えず，削除を妨げない

    def _todo(self, id: int) -> str:
        """保存形式の本文．"""
        row = self.db.execute("SELECT text FROM todos WHERE id=?", (id,)).fetchone()
        if row is None:
            raise WikiError(f"番号{id}のToDoは存在しない．")
        return row[0]

    def todo_add(self, text: str) -> dict:
        """先頭に積み，番号と本文を返す．"""
        with self._tx():
            stored, _ = self._parse_input(text)
            if stored == "":
                raise WikiError("ToDoが空である．")
            cur = self.db.execute(
                "INSERT INTO todos (text, pos) SELECT ?, coalesce(min(pos), 0) - 1 FROM todos", (stored,)
            )
            return {"id": cur.lastrowid, "text": self._render(stored)[0]}

    def todo_list(self, limit: int = 20) -> dict:
        """上から順に limit 件．"""
        rows = self.db.execute("SELECT id, text FROM todos ORDER BY pos LIMIT ?", (limit + 1,)).fetchall()
        return {
            "todos": [{"id": i, "text": self._render(t)[0]} for i, t in rows[:limit]],
            "truncated": len(rows) > limit,
        }

    def todos(self) -> list[dict]:
        """全ての ToDo．上から順．"""
        rows = self.db.execute("SELECT id, text FROM todos ORDER BY pos").fetchall()
        return [{"id": i, "text": self._render(t)[0]} for i, t in rows]

    def todo_remove(self, id: int) -> str:
        """消した本文を返す．"""
        with self._tx():
            text, _ = self._render(self._todo(id))
            self.db.execute("DELETE FROM todos WHERE id=?", (id,))
            return text

    def todo_defer(self, id: int) -> str:
        """末尾に送り，送った本文を返す．"""
        with self._tx():
            text, _ = self._render(self._todo(id))
            self.db.execute("UPDATE todos SET pos = (SELECT max(pos) + 1 FROM todos) WHERE id=?", (id,))
            return text
