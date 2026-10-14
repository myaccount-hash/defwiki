import sqlite3

import pytest

from defwiki.server import call
from defwiki.wiki import EXCERPT_LEN, Wiki, WikiError


@pytest.fixture
def w(tmp_path):
    wiki = Wiki(tmp_path / "w.db")
    yield wiki
    wiki.close()


def mk(w, term, description):
    r = w.create([{"term": term, "description": description}])
    return {"id": r["defs"][0]["id"], "warnings": r["warnings"]}


def shown(w, ids):
    """get の結果を `# [[識別子]] 用語` の見出しと説明の並びで表す．"""
    return "\n\n".join(f"# [[{d['id']}]] {d['term']}" + (f"\n{d['description']}" if d["description"] else "") for d in w.get(ids))


def refs(w, id, limit=20):
    """1つの定義についての references の結果．"""
    (r,) = w.references([id], limit)["results"]
    assert r.pop("id") == id
    return r


def test_create_get_and_reference(w):
    m = mk(w, "モデル", "")["id"]
    t = mk(w, "トークン", f"[[{m}|モデル]]が処理する文字列の単位．")["id"]
    assert shown(w, [t, m]) == f"# [[{t}]] トークン\n[[{m}|モデル]]が処理する文字列の単位．\n\n# [[{m}]] モデル"
    stored = w.db.execute("SELECT description FROM defs WHERE id=?", (t,)).fetchone()[0]
    assert stored == f"[[{m}]]が処理する文字列の単位．"


def test_rename_reflects_in_referrers(w):
    m = mk(w, "モデル", "")["id"]
    t = mk(w, "トークン", f"[[{m}|モデル]]の単位")["id"]
    w.rename([{"id": m, "term": "言語モデル"}])
    assert shown(w, [t]).endswith(f"[[{m}|言語モデル]]の単位")
    with pytest.raises(WikiError) as e:
        w.update([{"id": t, "description": f"[[{m}|モデル]]"}])
    assert "現在の用語は`言語モデル`" in str(e.value)


def test_reference_errors(w):
    with pytest.raises(WikiError, match="存在しない"):
        mk(w, "a", "[[zzzzzz|x]]")
    for bad in ["[[abc", "[[abcdef|x", "`[[abc", "``[[abc`", "\\[[abc"]:
        with pytest.raises(WikiError, match="形でない"):
            mk(w, "a", bad)
    for missing in ["[[ABCDEF|x]]", "[[abcdef]]", "[[[abcdef|x]]"]:
        with pytest.raises(WikiError, match="この呼び出しにない"):
            mk(w, "a", missing)
    assert w.db.execute("SELECT count(*) FROM defs").fetchone()[0] == 0


def test_multiple_errors_reported_together(w):
    with pytest.raises(WikiError) as e:
        mk(w, "a", "[[aaaaaa|x]] [[bbbbbb|y]]")
    assert len(e.value.errors) == 2


def test_escape(w):
    d = "`[[not a ref]]` と `` [[abcdef]]` `` と\n```\n[[\n```\nと ``` と `"
    i = mk(w, "esc", d)["id"]
    assert shown(w, [i]) == f"# [[{i}]] esc\n{d}"
    assert refs(w, i) == {"referrers": [], "truncated": False}


def test_create_cyclic_batch(w):
    m = mk(w, "モデル", "")["id"]
    r = w.create(
        [
            {"term": "A", "description": f"[[B]]と[[{m}|モデル]]の組．"},
            {"term": "B", "description": "[[A]]の対．[[B]]"},
        ]
    )
    a, b = (d["id"] for d in r["defs"])
    assert r["defs"] == [{"id": a, "term": "A"}, {"id": b, "term": "B"}]
    assert r["warnings"] == []
    assert shown(w, [a, b]) == f"# [[{a}]] A\n[[{b}|B]]と[[{m}|モデル]]の組．\n\n# [[{b}]] B\n[[{a}|A]]の対．[[{b}|B]]"
    assert {x["id"] for x in refs(w, b)["referrers"]} == {a, b}


def test_create_batch_is_atomic(w):
    with pytest.raises(WikiError) as e:
        w.create(
            [
                {"term": "A", "description": "[[X]] [[C]]"},
                {"term": "B", "description": "[[zzzzzz|x]]"},
            ]
        )
    assert e.value.errors == [
        "defs[0] `A`: `[[X]]`: 用語`X`の定義はこの呼び出しにない．",
        "defs[0] `A`: `[[C]]`: 用語`C`の定義はこの呼び出しにない．",
        "defs[1] `B`: `[[zzzzzz|x]]`: 識別子`zzzzzz`の定義は存在しない．",
    ]
    with pytest.raises(WikiError, match="重複"):
        w.create([{"term": "A", "description": ""}, {"term": "A", "description": ""}])
    assert w.db.execute("SELECT count(*) FROM defs").fetchone()[0] == 0
    a = mk(w, "A", "")["id"]
    with pytest.raises(WikiError, match="形でない"):
        w.update([{"id": a, "description": "[[A]]"}])


def test_term_after_ref_bracket(w):
    m = mk(w, "x", "")["id"]
    i = mk(w, "y", f"[[{m}|x]]]")["id"]
    assert shown(w, [i]).endswith(f"[[{m}|x]]]")


@pytest.mark.parametrize("term", ["", " a", "a ", "a\nb", "a[[b", "a]]b", "a]", "a`b", "a　"])
def test_term_rules(w, term):
    with pytest.raises(WikiError):
        mk(w, term, "")


def test_description_blank_lines_trimmed(w):
    i = mk(w, "a", "\n\n  \nline1\n\nline2\n \n\n")["id"]
    assert shown(w, [i]) == f"# [[{i}]] a\nline1\n\nline2"


def test_self_and_cyclic_reference(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", f"[[{a}|A]]")["id"]
    w.update([{"id": a, "description": f"[[{b}|B]] [[{a}|A]]"}])
    assert {r["id"] for r in refs(w, a)["referrers"]} == {a, b}
    with pytest.raises(WikiError, match="参照元"):
        w.delete([a])
    w.update([{"id": b, "description": ""}])
    w.delete([a])  # 自己参照のみなら削除できる
    assert refs(w, b) == {"referrers": [], "truncated": False}


def test_delete_blocked_then_allowed(w):
    m = mk(w, "m", "")["id"]
    t = mk(w, "t", f"[[{m}|m]]")["id"]
    with pytest.raises(WikiError, match=t):
        w.delete([m])
    w.delete([t])
    w.delete([m])
    with pytest.raises(WikiError, match="存在しない"):
        w.get([m])


def test_search(w):
    m = mk(w, "モデル", "")["id"]
    ids = [mk(w, f"語{i}", f"[[{m}|モデル]]の説明{i}")["id"] for i in range(5)]
    r, r4, none = w.search(["モデル", "説明4", "ない"], limit=3)["results"]
    assert r["query"] == "モデル" and r["truncated"] is True and len(r["hits"]) == 3
    assert r["hits"][0]["id"] == m
    assert [h["id"] for h in r4["hits"]] == [ids[4]] and r4["truncated"] is False
    assert none == {"query": "ない", "hits": [], "truncated": False}
    for i in range(16):
        mk(w, f"モデル{i}", "")
    assert len(call(w, "search", {"queries": ["モデル"]}).structured_content["results"][0]["hits"]) == 20


def test_longest(w):
    m = mk(w, "とても長い用語", "")["id"]
    a = mk(w, "a", f"[[{m}|とても長い用語]]あい")["id"]
    b = mk(w, "b", "あいう\n`[[x]]`")["id"]
    c = mk(w, "c", "かき")["id"]
    assert w.longest()["defs"] == [
        {"id": b, "term": "b", "length": 11},
        {"id": a, "term": "a", "length": 2},
        {"id": c, "term": "c", "length": 2},
        {"id": m, "term": "とても長い用語", "length": 0},
    ]
    assert [d["id"] for d in w.longest(limit=1)["defs"]] == [b]
    assert w.longest(limit=1)["truncated"] is True and w.longest(limit=4)["truncated"] is False
    assert call(w, "longest", {}).structured_content["defs"][0]["id"] == b
    assert call(w, "longest", {"limit": 0}).is_error
    assert call(w, "longest", {"with_description": True}).is_error
    for i in range(17):
        mk(w, f"d{i}", "")
    assert len(call(w, "longest", {}).structured_content["defs"]) == 20


def test_excerpt_does_not_cut_reference(w):
    m = mk(w, "とても長い用語" * 5, "")["id"]
    d = "あ" * 70 + f"[[{m}|{'とても長い用語' * 5}]]" + "い" * 50
    i = mk(w, "x", d)["id"]
    ex = w.search(["x"])["results"][0]["hits"][0]["excerpt"]
    assert ex == "あ" * 70 + f"[[{m}|{'とても長い用語' * 5}]]…"


def test_server_call(w):
    r = call(w, "create", {"defs": [{"term": "a", "description": ""}]})
    assert r.structured_content["defs"] == [{"id": (i := r.structured_content["defs"][0]["id"]), "term": "a"}]
    assert len(i) == 6
    assert call(w, "create", {"defs": []}).is_error
    assert call(w, "create", {"defs": [{"key": "A", "term": "a", "description": ""}]}).is_error
    assert call(w, "get", {"ids": [i]}).structured_content == {"defs": [{"id": i, "term": "a", "description": ""}]}
    assert call(w, "get", {"ids": ["BAD"]}).is_error
    assert call(w, "search", {"queries": ["a"], "extra": 1}).is_error
    assert call(w, "search", {"query": "a"}).is_error
    assert call(w, "search", {"queries": ["a"]}).structured_content["results"][0]["hits"][0]["id"] == i
    assert call(w, "rename", {"renames": [{"id": i, "term": "b"}]}).structured_content == {"warnings": []}
    assert call(w, "delete", {"ids": ["zzzzzz"]}).is_error


def test_warnings_on_create(w):
    r = mk(w, "モデル", "")
    m = r["id"]
    assert r["warnings"] == []
    r = mk(w, "トークン", "モデルが処理する単位．https://example.com/a を見よ．")
    assert r["warnings"] == [
        f"[[{r['id']}|トークン]]: 外部への参照を含む: `https://example.com/a`",
    ]
    assert w.update([{"id": r["id"], "description": f"[[{m}|モデル]]が処理する単位．"}]) == []
    r = mk(w, "モデル", f"[[{m}|モデル]]が処理する単位．")
    assert r["warnings"] == [
        f"[[{r['id']}|モデル]]: 説明が同一の定義がある: [[{w.search(['トークン'])['results'][0]['hits'][0]['id']}|トークン]]",
    ]


def test_create_dry_run(w):
    m = mk(w, "モデル", "")["id"]
    defs = [
        {"term": "A", "description": "https://example.com/a の一種．"},
        {"term": "B", "description": "[[A]]の別名．"},
    ]
    r = w.create(defs, dry_run=True)
    assert r == {
        "warnings": [
            "defs[0] `A`: 外部への参照を含む: `https://example.com/a`",
        ]
    }
    assert w.ids() == [m]
    with pytest.raises(WikiError, match="存在しない"):
        w.create([{"term": "B", "description": "[[zzzzzz|x]]"}], dry_run=True)
    r = call(w, "create", {"defs": defs, "dry_run": True})
    assert "defs" not in r.structured_content and len(r.structured_content["warnings"]) == 1
    assert w.ids() == [m]
    assert len(w.create(defs)["defs"]) == 2


def test_warnings_on_rename_and_delete(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", f"[[{a}|A]]とCの組．")["id"]
    assert w.rename([{"id": a, "term": "C"}]) == []
    assert w.delete([b]) == [f"[[{a}|C]]: 参照も被参照もなくなった．"]


def test_merge(w):
    a = mk(w, "モデル", "")["id"]
    b = mk(w, "言語モデル", "")["id"]
    t = mk(w, "トークン", f"[[{a}|モデル]]の単位．`[[{a}]]`と[[{a}|モデル]]")["id"]
    u = mk(w, "文脈", f"[[{a}|モデル]]と[[{b}|言語モデル]]")["id"]
    assert w.merge([{"id": a, "into": b}]) == []
    with pytest.raises(WikiError, match="存在しない"):
        w.get([a])
    assert shown(w, [t, u]) == (
        f"# [[{t}]] トークン\n[[{b}|言語モデル]]の単位．`[[{a}]]`と[[{b}|言語モデル]]\n\n"
        f"# [[{u}]] 文脈\n[[{b}|言語モデル]]と[[{b}|言語モデル]]"
    )
    assert refs(w, b) == {"referrers": [{"id": t, "term": "トークン"}, {"id": u, "term": "文脈"}], "truncated": False}
    assert refs(w, b, limit=1) == {"referrers": [{"id": t, "term": "トークン"}], "truncated": True}
    assert call(w, "references", {"ids": [b], "limit": 101}).is_error
    assert w.db.execute("SELECT count(*) FROM refs WHERE src=? OR dst=?", (a, a)).fetchone()[0] == 0


def test_merge_many_referrers(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", "")["id"]
    w.create([{"term": f"t{i}", "description": f"[[{a}|A]]"} for i in range(25)])
    w.merge([{"id": a, "into": b}])
    assert w.db.execute("SELECT count(*) FROM refs WHERE dst=?", (a,)).fetchone()[0] == 0
    assert len(refs(w, b, limit=100)["referrers"]) == 25


def test_merge_errors(w):
    a = mk(w, "A", "")["id"]
    with pytest.raises(WikiError, match="それ自身"):
        w.merge([{"id": a, "into": a}])
    with pytest.raises(WikiError, match="存在しない"):
        w.merge([{"id": a, "into": "zzzzzz"}])
    with pytest.raises(WikiError, match="存在しない"):
        w.merge([{"id": "zzzzzz", "into": a}])
    assert shown(w, [a]) == f"# [[{a}]] A"


def test_warnings_on_merge(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", f"[[{a}|A]]")["id"]
    # 統合先が統合元を参照していれば自己参照になり，他との参照がなければ孤立する
    assert w.merge([{"id": a, "into": b}]) == [f"[[{b}|B]]: 参照も被参照もない．"]
    assert shown(w, [b]) == f"# [[{b}]] B\n[[{b}|B]]"

    c = mk(w, "C", f"[[{b}|B]]")["id"]
    d = mk(w, "D", f"[[{c}|C]]の例．")["id"]
    e = mk(w, "E", f"[[{b}|B]]の例．")["id"]
    f = mk(w, "F", "")["id"]
    w.update([{"id": c, "description": f"[[{f}|F]]"}])
    # 統合元だけが参照していた定義は孤立し，書き換えた説明は他と同一になりうる
    assert w.merge([{"id": c, "into": b}]) == [
        f"[[{d}|D]]: 説明が同一の定義がある: [[{e}|E]]",
        f"[[{f}|F]]: 参照も被参照もなくなった．",
    ]


def test_server_merge(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", "")["id"]
    mk(w, "C", f"[[{a}|A]]と[[{b}|B]]")
    assert call(w, "merge", {"merges": [{"id": a, "into": b}]}).structured_content == {"warnings": []}
    assert call(w, "merge", {"merges": [{"id": a, "into": b}]}).is_error
    assert call(w, "merge", {"merges": [{"id": b}]}).is_error


def test_check(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", "Aを含む．")["id"]
    c = mk(w, "B", f"[[{a}|A]]")["id"]
    r = w.check()
    assert r["isolated"] == [{"id": b, "term": "B"}]
    assert "duplicate_terms" not in r
    assert r["duplicate_descriptions"] == [] and r["external"] == []
    assert r["counts"] == {"isolated": 1, "duplicate_descriptions": 0, "external": 0}
    assert r["truncated"] == {"isolated": False, "duplicate_descriptions": False, "external": False}
    mk(w, "D", "")
    r = w.check(limit=1)
    assert r["isolated"] == [{"id": b, "term": "B"}] and r["counts"]["isolated"] == 2
    assert r["truncated"]["isolated"] is True
    assert call(w, "check", {"limit": 0}).is_error


def test_server_rules_and_warnings(w):
    from defwiki.server import RULES

    assert call(w, "rules", {}).content[0].text == RULES
    r = call(w, "create", {"defs": [{"term": "a", "description": ""}]})
    i = r.structured_content["defs"][0]["id"]
    assert r.structured_content["warnings"] == []
    assert call(w, "update", {"updates": [{"id": i, "description": "x"}]}).structured_content == {"warnings": [f"[[{i}|a]]: 参照も被参照もない．"]}
    assert call(w, "check", {}).structured_content["isolated"] == [{"id": i, "term": "a"}]


def test_export_markdown(w):
    from defwiki.export import wiki_markdown

    assert wiki_markdown(w) == ""
    m = mk(w, "a]b", "")["id"]
    t = mk(w, "トークン", f"[[{m}|a]b]]が処理する`[[x]]`．")["id"]
    assert wiki_markdown(w) == (
        f'<a id="{m}"></a>\n\n## a]b\n\n'
        f'<a id="{t}"></a>\n\n## トークン\n\n[a\\]b](#{m})が処理する`[[x]]`．\n'
    )


def test_export_todo(w):
    from defwiki.export import todo_markdown

    assert todo_markdown(w) == ""
    m = mk(w, "a]b", "")["id"]
    a = w.todo_add(["a"])["todos"][0]["id"]
    b = w.todo_add([f"[[{m}|a]b]]を直す．\n2行目"])["todos"][0]["id"]
    assert todo_markdown(w) == (
        f'<a id="todo-{b}"></a>\n\n## {b}\n\n[a\\]b](wiki.md#{m})を直す．\n2行目\n\n'
        f'<a id="todo-{a}"></a>\n\n## {a}\n\na\n'
    )


def test_export_todo_backrefs(w):
    from defwiki.export import wiki_markdown

    m = mk(w, "m", "")["id"]
    t = mk(w, "t", f"[[{m}|m]]の単位．")["id"]
    a = w.todo_add([f"[[{m}|m]]と[[{m}|m]]"])["todos"][0]["id"]
    w.todo_add(["x"])
    b = w.todo_add([f"[[{t}|t]]と[[{m}|m]]"])["todos"][0]["id"]
    assert wiki_markdown(w) == (
        f'<a id="{m}"></a>\n\n## m\n\nToDo: [{b}](todo.md#todo-{b})，[{a}](todo.md#todo-{a})\n\n'
        f'<a id="{t}"></a>\n\n## t\n\n[m](#{m})の単位．\n\nToDo: [{b}](todo.md#todo-{b})\n'
    )


def test_export_files(w, tmp_path):
    from defwiki.export import export, todo_markdown, wiki_markdown

    mk(w, "a", "")
    w.todo_add(["b"])
    out = tmp_path / "x" / "y"
    export(w, out)
    assert (out / "wiki.md").read_text(encoding="utf-8") == wiki_markdown(w)
    assert (out / "todo.md").read_text(encoding="utf-8") == todo_markdown(w)


def test_todo_stack_and_defer(w):
    a = w.todo_add(["a"])["todos"][0]["id"]
    b = w.todo_add(["b"])["todos"][0]["id"]
    c = w.todo_add(["c"])["todos"][0]["id"]
    assert [t["text"] for t in w.todo_list()["todos"]] == ["c", "b", "a"]
    assert w.todo_defer([c]) == {"todos": [{"id": c, "text": "c"}]}
    assert [t["id"] for t in w.todo_list()["todos"]] == [b, a, c]
    assert w.todo_remove([a]) == {"todos": [{"id": a, "text": "a"}]}
    d = w.todo_add(["d"])["todos"][0]["id"]
    assert d not in (a, b, c)
    assert [t["text"] for t in w.todo_list()["todos"]] == ["d", "b", "c"]
    with pytest.raises(WikiError, match="存在しない"):
        w.todo_remove([a])
    with pytest.raises(WikiError, match="空"):
        w.todo_add([" "])
    assert w.todo_list(limit=2) == {"todos": [{"id": d, "text": "d"}, {"id": b, "text": "b"}], "truncated": True}
    assert w.todo_list(limit=3)["truncated"] is False


def test_todo_references(w):
    m = mk(w, "モデル", "")["id"]
    t = mk(w, "トークン", "")["id"]
    with pytest.raises(WikiError, match="現在の用語は`モデル`"):
        w.todo_add([f"[[{m}|トークン]]を見直す"])
    with pytest.raises(WikiError, match="存在しない"):
        w.todo_add(["[[zzzzzz|モデル]]を見直す"])
    assert w.todo_list() == {"todos": [], "truncated": False}
    n = w.todo_add([f"[[{m}|モデル]]と[[{t}|トークン]]を見直す．`[[{m}]]`"])["todos"][0]["id"]
    # ToDoからの参照は被参照に数えない
    assert refs(w, m) == {"referrers": [], "truncated": False}
    assert {d["id"] for d in w.check()["isolated"]} == {m, t}
    w.rename([{"id": m, "term": "言語モデル"}])
    assert w.todo_list()["todos"][0]["text"] == f"[[{m}|言語モデル]]と[[{t}|トークン]]を見直す．`[[{m}]]`"
    w.merge([{"id": t, "into": m}])
    assert w.todo_list()["todos"][0]["text"] == f"[[{m}|言語モデル]]と[[{m}|言語モデル]]を見直す．`[[{m}]]`"
    w.delete([m])
    assert w.todo_remove([n])["todos"][0]["text"] == f"言語モデルと言語モデルを見直す．`[[{m}]]`"


def test_todo_reference_to_deleted_term_with_bracket(w):
    a = mk(w, "a[", "")["id"]
    w.todo_add([f"[[{a}|a[]][b"])
    w.delete([a])
    assert w.todo_list()["todos"][0]["text"] == "`a[`[b"


@pytest.mark.parametrize("version", [0, 2])
def test_reject_unsupported_database_without_changes(tmp_path, version):
    path = tmp_path / "old.db"
    w = Wiki(path)
    m = mk(w, "モデル", "")["id"]
    old = [f"[[{m}|モデル]]を見直す", f"[[{m}|トークン]]と[[zzzzzz|文書]]", "[[壊れた参照", "参照なし"]
    w.db.executemany("INSERT INTO todos (text, pos) VALUES (?, ?)", list(zip(old, range(4))))
    w.db.execute(f"PRAGMA user_version = {version}")
    w.close()
    before = path.read_bytes()
    with pytest.raises(WikiError, match=f"user_version={version}"):
        Wiki(path)
    assert path.read_bytes() == before
    with sqlite3.connect(path) as db:
        assert db.execute("PRAGMA user_version").fetchone()[0] == version
        assert [r[0] for r in db.execute("SELECT text FROM todos ORDER BY pos")] == old


def test_new_database_version_and_reopen(tmp_path):
    path = tmp_path / "new.db"
    w = Wiki(path)
    assert w.db.execute("PRAGMA user_version").fetchone()[0] == 1
    d = mk(w, "モデル", "説明")
    w.close()
    w = Wiki(path)
    assert w.get([d["id"]])[0]["description"] == "説明"
    w.close()


def test_server_todo(w):
    r = call(w, "todo_add", {"texts": ["\nx\n"]}).structured_content
    assert r == {"todos": [{"id": (i := r["todos"][0]["id"]), "text": "x"}]}
    assert call(w, "todo_list", {}).structured_content == {"todos": [{"id": i, "text": "x"}], "truncated": False}
    assert call(w, "todo_defer", {"ids": [i]}).structured_content == {"todos": [{"id": i, "text": "x"}]}
    assert call(w, "todo_remove", {"ids": [i]}).structured_content == {"todos": [{"id": i, "text": "x"}]}
    assert call(w, "todo_remove", {"ids": [i]}).is_error
    assert call(w, "todo_add", {"texts": [""]}).is_error
    assert call(w, "todo_add", {"texts": ["[[zzzzzz|x]]"]}).is_error
    assert call(w, "todo_defer", {"ids": ["1"]}).is_error
    assert call(w, "todo_list", {"limit": 101}).is_error


def test_excerpt_around_match(w):
    m = mk(w, "モデル", "")["id"]
    d = "あ" * 30 + f"[[{m}|モデル]]" + "い" * 10 + "目印" + "う" * 100
    i = mk(w, "x", d)["id"]
    ex = w.search(["目印"])["results"][0]["hits"][0]["excerpt"]
    assert ex == "…" + f"[[{m}|モデル]]" + "い" * 10 + "目印" + "う" * (EXCERPT_LEN - 22) + "…"
    # 用語で一致した定義は先頭から切る
    assert w.search(["x"])["results"][0]["hits"][0]["excerpt"] == d[:EXCERPT_LEN] + "…"
    # 一致が長ければ一致の終わりまで延ばす
    q = "う" * 100
    assert w.search([q])["results"][0]["hits"][0]["excerpt"] == "…" + f"[[{m}|モデル]]" + "い" * 10 + "目印" + q


def test_update_edits(w):
    m = mk(w, "モデル", "")["id"]
    i = mk(w, "x", f"[[{m}|モデル]]が処理するあ．いあ．")["id"]
    w.update([{"id": i, "edits": [{"old": "処理する", "new": "扱う"}, {"old": "いあ", "new": "う"}]}])
    assert shown(w, [i]) == f"# [[{i}]] x\n[[{m}|モデル]]が扱うあ．う．"
    # 参照も提示形式で照合し，置換の結果を検証する
    w.update([{"id": i, "edits": [{"old": f"[[{m}|モデル]]が", "new": ""}]}])
    assert refs(w, m) == {"referrers": [], "truncated": False}
    with pytest.raises(WikiError, match="現在の用語は`モデル`"):
        w.update([{"id": i, "edits": [{"old": "扱う", "new": f"[[{m}|x]]"}]}])
    with pytest.raises(WikiError) as e:
        w.update([{"id": i, "edits": [{"old": "あ", "new": "あ"}, {"old": "ない", "new": ""}, {"old": "う", "new": "あ"}]}])
    assert e.value.errors == [
        "updates[0]: edits[1]: `old`が説明に現れない．",
        "updates[0]: edits[2]: `old`が説明に2回現れる．一意に定まるよう前後を含める．",
    ]
    assert shown(w, [i]) == f"# [[{i}]] x\n扱うあ．う．"
    assert "warnings" in call(w, "update", {"updates": [{"id": i, "edits": [{"old": "．う", "new": "．え"}]}]}).structured_content
    assert call(w, "update", {"updates": [{"id": i}]}).is_error
    assert call(w, "update", {"updates": [{"id": i, "description": "", "edits": [{"old": "a", "new": ""}]}]}).is_error
    assert call(w, "update", {"updates": [{"id": i, "edits": [{"old": "", "new": "a"}]}]}).is_error


def test_batch_writes_are_atomic(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", "")["id"]
    assert w.update([{"id": a, "description": f"[[{b}|B]]の対．"}, {"id": b, "description": f"[[{a}|A]]の対．"}]) == []
    assert shown(w, [a, b]) == f"# [[{a}]] A\n[[{b}|B]]の対．\n\n# [[{b}]] B\n[[{a}|A]]の対．"
    with pytest.raises(WikiError) as e:
        w.update([
            {"id": a, "description": "x"},
            {"id": b, "edits": [{"old": "ない", "new": ""}]},
            {"id": a, "description": "y"},
            {"id": "zzzzzz", "description": ""},
        ])
    assert e.value.errors == [
        "updates[1]: edits[0]: `old`が説明に現れない．",
        f"updates[2]: 識別子`{a}`が重複している．",
        "updates[3]: 識別子`zzzzzz`の定義は存在しない．",
    ]
    with pytest.raises(WikiError, match=r"renames\[1\]: 用語が空"):
        w.rename([{"id": a, "term": "C"}, {"id": b, "term": ""}])
    assert w.get([a])[0]["term"] == "A"
    # 互いに参照する定義は，まとめてなら削除できる
    with pytest.raises(WikiError, match=r"ids\[0\]: 参照されている"):
        w.delete([a])
    c = mk(w, "C", f"[[{a}|A]]")["id"]
    with pytest.raises(WikiError, match=r"ids\[0\]: .*参照元: \[\[" + c):
        w.delete([a, b])
    w.update([{"id": c, "description": f"[[{b}|B]]"}])
    with pytest.raises(WikiError, match=r"ids\[1\]: .*参照元: \[\[" + c):
        w.delete([a, b])
    w.update([{"id": c, "description": ""}])
    assert w.delete([a, b]) == []
    assert w.ids() == [c]


def test_merge_in_order(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", "")["id"]
    c = mk(w, "C", "")["id"]
    d = mk(w, "D", f"[[{a}|A]]と[[{b}|B]]")["id"]
    assert w.merge([{"id": a, "into": b}, {"id": b, "into": c}]) == []
    assert shown(w, [d]) == f"# [[{d}]] D\n[[{c}|C]]と[[{c}|C]]"
    with pytest.raises(WikiError) as e:
        w.merge([{"id": c, "into": d}, {"id": c, "into": d}])
    assert e.value.errors == [f"merges[1]: 識別子`{c}`の定義は存在しない．"]
    assert w.ids() == [c, d]


def test_references_batch(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", f"[[{a}|A]]")["id"]
    assert w.references([a, b]) == {
        "results": [
            {"id": a, "referrers": [{"id": b, "term": "B"}], "truncated": False},
            {"id": b, "referrers": [], "truncated": False},
        ]
    }
    with pytest.raises(WikiError, match="zzzzzz"):
        w.references([a, "zzzzzz"])


def test_dry_run_on_all_writes(w):
    a = mk(w, "A", "")["id"]
    b = mk(w, "B", f"[[{a}|A]]")["id"]
    before = shown(w, [a, b])
    assert w.update([{"id": b, "description": "https://example.com/x"}], dry_run=True) == [
        f"[[{b}|B]]: 参照も被参照もない．",
        f"[[{b}|B]]: 外部への参照を含む: `https://example.com/x`",
    ]
    assert w.rename([{"id": a, "term": "C"}], dry_run=True) == []
    assert w.delete([b], dry_run=True) == [f"[[{a}|A]]: 参照も被参照もなくなった．"]
    assert w.merge([{"id": a, "into": b}], dry_run=True) == [f"[[{b}|B]]: 参照も被参照もない．"]
    with pytest.raises(WikiError, match="参照されている"):
        w.delete([a], dry_run=True)
    assert shown(w, [a, b]) == before
    r = call(w, "delete", {"ids": [b], "dry_run": True})
    assert r.structured_content == {"warnings": [f"[[{a}|A]]: 参照も被参照もなくなった．"]}
    assert w.ids() == [a, b]


def test_todo_batch(w):
    r = w.todo_add(["a", "b"])["todos"]
    a, b = (t["id"] for t in r)
    assert r == [{"id": a, "text": "a"}, {"id": b, "text": "b"}]
    c = w.todo_add(["c"])["todos"][0]["id"]
    assert [t["id"] for t in w.todo_list()["todos"]] == [c, a, b]
    with pytest.raises(WikiError) as e:
        w.todo_add(["d", " ", "[[zzzzzz|x]]"])
    assert [m.split(":")[0] for m in e.value.errors] == ["texts[1]", "texts[2]"]
    assert w.todo_defer([c, a])["todos"] == [{"id": c, "text": "c"}, {"id": a, "text": "a"}]
    assert [t["id"] for t in w.todo_list()["todos"]] == [b, c, a]
    with pytest.raises(WikiError, match=r"ids\[1\]: 番号"):
        w.todo_remove([b, 999999])
    assert len(w.todo_list()["todos"]) == 3
    assert [t["id"] for t in w.todo_remove([a, b])["todos"]] == [a, b]
    assert [t["id"] for t in w.todo_list()["todos"]] == [c]


def test_create_local_references_do_not_search_existing_terms(w):
    existing = mk(w, "モデル", "既存の説明．")["id"]
    with pytest.raises(WikiError, match="この呼び出しにない"):
        mk(w, "トークン", "[[モデル]]")
    result = w.create([
        {"term": "モデル", "description": "新しい説明．"},
        {"term": "トークン", "description": f"[[モデル]]と[[{existing}|モデル]]"},
    ])
    new, token = [d["id"] for d in result["defs"]]
    assert w.get([token])[0]["description"] == f"[[{new}|モデル]]と[[{existing}|モデル]]"
    assert {r["id"] for r in refs(w, new)["referrers"]} == {token}
    assert {r["id"] for r in refs(w, existing)["referrers"]} == {token}


@pytest.mark.parametrize("term", ["日本語", "abcdef", "A|B", "角[括弧]内", "$名前", "二つの 語"])
def test_create_local_reference_term_characters(w, term):
    result = w.create([{"term": term, "description": f"[[{term}]]"}])
    id = result["defs"][0]["id"]
    assert w.get([id])[0]["description"] == f"[[{id}|{term}]]"
    assert w.db.execute("SELECT description FROM defs WHERE id=?", (id,)).fetchone()[0] == f"[[{id}]]"


def test_create_id_reference_takes_precedence(w):
    with pytest.raises(WikiError, match="存在しない"):
        w.create([{"term": "abcdef|名前", "description": "[[abcdef|名前]]"}])
    assert w.ids() == []


def test_local_references_rejected_outside_create(w):
    id = mk(w, "A", "元の説明．")["id"]
    with pytest.raises(WikiError, match="形でない"):
        w.update([{"id": id, "edits": [{"old": "元の説明．", "new": "[[A]]"}]}])
    with pytest.raises(WikiError, match="形でない"):
        w.todo_add(["[[A]]"])
    assert w.get([id])[0]["description"] == "元の説明．"
    assert w.todos() == []


def test_create_mcp_contract(w):
    assert call(w, "create", {"defs": [{"key": "a", "term": "A", "description": ""}]}).is_error
    duplicate = {"defs": [{"term": "A", "description": ""}, {"term": "A", "description": ""}]}
    assert call(w, "create", duplicate).is_error
    assert call(w, "create", {**duplicate, "dry_run": True}).is_error
    assert w.ids() == []
    result = call(w, "create", {"defs": [{"term": "A", "description": "[[A]]"}]})
    assert not result.is_error
    assert set(result.structured_content["defs"][0]) == {"id", "term"}
