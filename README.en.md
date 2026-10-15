[日本語](README.md) | English

# defwiki

defwiki is an MCP server that provides a knowledge base exclusively for AI agents. It is not primarily meant to be read by humans.
By restricting entries to the form of a glossary, it lets AI agents build up a knowledge base sustainably.

> [!NOTE]
> The operating rules, the MCP server instructions, and the samples are currently written in Japanese, so agents will tend to write the wiki in Japanese.

When a human wants to inspect the contents, the `defwiki-export` script exports them to Markdown. The following samples were exported this way.
- [examples/wiki.md](examples/wiki.md): an AI-generated wiki consisting of 941 definitions.
- [examples/todo.md](examples/todo.md): an AI-generated to-do list for the wiki.

Below are screenshots of the samples.
The to-do list shows the AI agent autonomously trying to fix the wiki and to abstract concepts that share a similar structure.

<p align="center">
  <img src="docs/images/wiki-sample.png" alt="Rendering of examples/wiki.md" width="49%">
  <img src="docs/images/todo-sample.png" alt="Rendering of examples/todo.md" width="49%">
</p>

The MCP server specification is in [SPEC.md](SPEC.md), and the operating rules that agents follow are in [src/defwiki/rules.md](src/defwiki/rules.md) (both in Japanese).

## Design principles

defwiki follows the principle of "maximum explanation with minimum description".
Free-form knowledge bases have the following drawbacks:

- They keep growing until neither humans nor AI can grasp the whole.
- Relations between pieces of knowledge are not explicit, so AI agents cannot "build" new knowledge on top of existing knowledge.

To prevent this, defwiki imposes the following constraints:

- Entries are restricted to the form of a glossary. Knowledge is connected through references between definitions, so new definitions can be written on top of existing ones. Each concept is written in exactly one definition, and every other place refers to it. This is the DRY principle applied to knowledge.
- The wiki is a "closed system" with no external dependencies. Explanations do not refer to external documents and are complete with the definitions inside the wiki alone.
- Concepts are treated as "definitions" that do not depend on their position or order in a document, so they can be carried over to other contexts.

Under these principles, defwiki holds two things: the wiki (glossary) and the to-do list.

## The wiki

The wiki is an unordered set of definitions. A definition consists of an "identifier", a "term", and a "description".
The following example shows definitions of token, model, and context.

```markdown
# [[k3f9x2]] Token
The unit of string that a [[p8m2qa|model]] processes.

# [[p8m2qa]] Model
A function that takes a [[w7d4ne|context]] and predicts the next [[k3f9x2|token]].

# [[w7d4ne]] Context
The sequence of [[k3f9x2|tokens]] that a [[p8m2qa|model]] receives at once.
```

An identifier is a 6-character string of `[a-z0-9]` randomly assigned by the MCP server. Inside a description, other definitions are referenced in the form `[[identifier|term]]`.

`create` can create multiple definitions at once. Definitions created in the same call reference each other with `[[term]]`, so circular references can be written as well. Duplicate terms are forbidden within a single batch, but a term already used by an existing definition is allowed.

```json
{
  "defs": [
    {"term": "Model", "description": "A function that predicts [[Token]]s."},
    {"term": "Token", "description": "The unit of string that a [[Model]] processes."}
  ]
}
```

`[[term]]` refers only to the definitions being created in that call and never looks up existing definitions. References to existing definitions, retrieval results, `update`, and to-dos use `[[identifier|term]]`. The `[[identifier|term]]` form is always interpreted as a reference by ID.

## The to-do list

The to-do list is an ordered list that AI agents read and update. defwiki includes it so that problems not fixed on the spot can be carried over across tasks.
When an AI agent notices such a problem during its work, it adds it to the top as a to-do.
A to-do consists of a number and a body, and the body can reference definitions in the `[[identifier|term]]` form, just like a description.
At the start of a task, the agent looks at the to-do list, handles and removes the to-dos it can finish first, and moves the ones it will not work on to the end.

## Operating rules

In addition to the data format, defwiki provides operating rules that AI agents follow, because format constraints alone cannot uphold the design principles.

The glossary format limits entries to a set of definitions. It does not, however, decide what becomes a definition or how it is written. Writing without rules accumulates duplicate definitions, vague descriptions, and transient information, leading to the same drawbacks as a free-form knowledge base.

The operating rules align the following decisions across agents:

- What to write: only confident, permanent knowledge, with its scope and conditions fully stated.
- How to write: reference existing definitions and minimize the amount of description through abstraction.
- When to fix: fix a noticed problem on the spot, or push it onto the to-do list.

Some of the rules are checked mechanically by `check`. Semantic duplication and room for abstraction cannot be detected mechanically, so those judgments are left to agents as rules. The rules are handed to agents through the `rules` tool.

## Installation

### Requirements

- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/)

### Steps

Clone the repository and install the dependencies in that directory.

```bash
git clone https://github.com/myaccount-hash/defwiki.git /path/to/defwiki
cd /path/to/defwiki
uv sync
```

Register the `defwiki` command with your MCP client. For Claude Code:

```bash
claude mcp add defwiki -- uv run --directory /path/to/defwiki defwiki
```

To write it in a configuration file:

```json
{
  "mcpServers": {
    "defwiki": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/defwiki", "defwiki"]
    }
  }
}
```

After registering, set up the system prompt so that the AI agent uses defwiki. For example:

```
Use the defwiki MCP when saving new knowledge and when looking up knowledge.
```

### Database location

The wiki and the to-do list are stored in a single database file. Its location is specified by the environment variable `DEFWIKI_DB`. The default is `~/.defwiki/wiki.db`. `defwiki-export` reads from the same location.

## Inspecting the contents

`defwiki-export` writes the whole wiki to `wiki.md` and the whole to-do list to `todo.md`. The output directory is specified with `--out-dir`. The default is `exports`.
Both are Markdown with references converted into clickable links. When rendered, identifiers are not shown. References in `todo.md` link to definitions in `wiki.md`, and at the end of each definition in `wiki.md` are links to the to-dos that reference it.

```bash
uv run defwiki-export --out-dir exports
```

## License

[MIT](LICENSE)
