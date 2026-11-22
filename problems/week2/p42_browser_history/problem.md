# P42 · Mini-project: browser history

Simulate a browser's back/forward buttons with two stacks. The browser starts on `home`. Read commands until `Q`:

- `visit url` — go to url; the forward history is cleared
- `back` — go back one page (stay put if there is no history)
- `forward` — go forward one page (stay put if there is none)

After every command, print the current page.

**Focus:** two stacks plus a `current` variable. In C, store URLs as `char[32]` arrays and copy with `strcpy`. **Rust:** `Vec<String>` stacks — moving a `String` from one stack to another is a move, not a copy.

**Sample input** (also in `in.txt`):
```
visit a
visit b
back
back
back
forward
visit c
forward
Q
```
