# P37 · Balanced brackets

Read a line. Considering only the characters `()[]{}`, print `Balanced` if every bracket is closed by the matching type in the right order, else `Not balanced`.

Samples: `{[()()]}` → `Balanced` · `([)]` → `Not balanced`

**Focus:** a stack of open brackets. In C, an array plus a top index is a stack. In Rust, `Vec<char>` with `push`/`pop` — `pop()` returns `Option<char>`, so `match` it.

**Sample input** (also in `in.txt`):
```
{[()()]}
```
