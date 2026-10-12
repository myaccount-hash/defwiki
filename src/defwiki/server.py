"""defwiki の MCP サーバ（stdio）．

データベースの場所は環境変数 DEFWIKI_DB で指定する．既定は ~/.defwiki/wiki.db．
"""

from __future__ import annotations

import json
from importlib import resources
from typing import Any, Callable

import anyio
import jsonschema
import mcp_types as types
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server

from .wiki import Wiki, WikiError, default_db

_FILES = resources.files(__package__)
TOOL_DEFS: list[dict[str, Any]] = json.loads(_FILES.joinpath("tools.json").read_text("utf-8"))
RULES = _FILES.joinpath("rules.md").read_text("utf-8")
INSTRUCTIONS = """\
defwikiは，LLMが作業に用いる概念の定義の体系を保持する．
- 書込む前に`rules`で運用規則を読む．
- 定義を作る前に`search`で既存の定義を探し，あれば作らずに参照する．
- 書込みが返す警告は運用規則への違反の疑いである．解消するか，違反でないと確かめる．
- 作業中に見つけた問題は，その場で直すか`todo_add`で積む．
- 書込みを終えたら`check`でWiki全体を点検する．
"""
_BY_NAME = {t["name"]: t for t in TOOL_DEFS}
_TOOLS = [
    types.Tool(
        name=t["name"],
        description=t["description"],
        input_schema=t["inputSchema"],
        output_schema=t.get("outputSchema"),
    )
    for t in TOOL_DEFS
]


def _text(s: str, is_error: bool = False) -> types.CallToolResult:
    return types.CallToolResult(content=[types.TextContent(type="text", text=s)], is_error=is_error)


def _structured(d: dict) -> types.CallToolResult:
    return types.CallToolResult(
        content=[types.TextContent(type="text", text=json.dumps(d, ensure_ascii=False))],
        structured_content=d,
    )


def _ok(warnings: list[str]) -> types.CallToolResult:
    return _text("\n".join(["ok", *(f"警告: {w}" for w in warnings)]))


_HANDLERS: dict[str, Callable[[Wiki, dict[str, Any]], types.CallToolResult]] = {
    "rules": lambda wiki, args: _text(RULES),
    "check": lambda wiki, args: _structured(wiki.check(args.get("limit", 20))),
    "get": lambda wiki, args: _text(wiki.get(args["ids"])),
    "search": lambda wiki, args: _structured(wiki.search(args["queries"], args.get("limit", 10))),
    "longest": lambda wiki, args: _structured(
        wiki.longest(args.get("limit", 5 if args.get("with_description") else 20), args.get("with_description", False))
    ),
    "references": lambda wiki, args: _structured(wiki.references(args["id"], args.get("limit", 20))),
    "create": lambda wiki, args: _structured(wiki.create(args["defs"], args.get("dry_run", False))),
    "update": lambda wiki, args: _ok(wiki.update(args["id"], args.get("description"), args.get("edits"))),
    "rename": lambda wiki, args: _ok(wiki.rename(args["id"], args["term"])),
    "delete": lambda wiki, args: _ok(wiki.delete(args["id"])),
    "merge": lambda wiki, args: _ok(wiki.merge(args["id"], args["into"])),
    "todo_add": lambda wiki, args: _structured(wiki.todo_add(args["text"])),
    "todo_list": lambda wiki, args: _structured(wiki.todo_list(args.get("limit", 20))),
    "todo_remove": lambda wiki, args: _structured({"text": wiki.todo_remove(args["id"])}),
    "todo_defer": lambda wiki, args: _structured({"text": wiki.todo_defer(args["id"])}),
}
assert _HANDLERS.keys() == _BY_NAME.keys()


def call(wiki: Wiki, name: str, args: dict[str, Any]) -> types.CallToolResult:
    tool = _BY_NAME.get(name)
    if tool is None:
        return _text(f"不明なツール: {name}", True)
    try:
        jsonschema.validate(args, tool["inputSchema"])
    except jsonschema.ValidationError as e:
        return _text(f"引数が不正: {e.message}", True)
    try:
        return _HANDLERS[name](wiki, args)
    except WikiError as e:
        return _text(str(e), True)


def make_server(wiki: Wiki) -> Server:
    async def list_tools(ctx, params) -> types.ListToolsResult:
        return types.ListToolsResult(tools=_TOOLS)

    async def call_tool(ctx, params: types.CallToolRequestParams) -> types.CallToolResult:
        return call(wiki, params.name, dict(params.arguments or {}))

    return Server(
        "defwiki", version="0.1.0", instructions=INSTRUCTIONS, on_list_tools=list_tools, on_call_tool=call_tool
    )


def main() -> None:
    db = default_db()
    db.parent.mkdir(parents=True, exist_ok=True)
    wiki = Wiki(db)
    server = make_server(wiki)

    async def run():
        async with stdio_server() as (r, w):
            await server.run(r, w, server.create_initialization_options())

    try:
        anyio.run(run)
    finally:
        wiki.close()


if __name__ == "__main__":
    main()
