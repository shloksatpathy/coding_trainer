# PLAN: own interface, fully local, minimal disk use

## Goal

Replace the browser UI (`app.py` + `static/index.html`) with an interface the program draws itself, so it runs with no browser and no local web server, and cut the project's disk footprint.

## Where we are (measured 2026-11-22)

| Item | Size / state |
| --- | --- |
| `trainer.py` (CLI + checker) | 246 lines, stdlib only |
| `app.py` + `static/index.html` (web UI) | 287 lines, needs a browser + local HTTP server |
| `problems/` | 1,022 files, 17 MB |
| └ 20 large test inputs and their outputs | **15.9 MB of the 16.9 MB of test data** |
| `.git` | 12 MB (history already contains the large tests) |
| Python | 3.13 from nix: `curses` ✅, `tkinter` ❌ (no Tcl/Tk installed) |
| Toolchains | gcc/g++ 15.3 ✅, rustc ⚠️ (`rustup default stable` not run yet) |
| Editor | `$EDITOR=nvim` |

## Decision: a terminal UI (curses), editing in `$EDITOR`

| Option | Extra disk | New dependencies | Notes |
| --- | --- | --- | --- |
| **curses TUI (chosen)** | **~15 KB (one file)** | **none — in Python's stdlib** | Runs in any terminal, also over SSH. Real editing happens in your own editor. |
| tkinter window | ~10–15 MB Tcl/Tk | must add tk to the nix Python | Proper window, built-in text widget, but not installed today. |
| Native Rust GUI (egui/iced) | 5–10 MB binary, ~0.5–1 GB `target/` while building | Rust crates | Most work, biggest build footprint. |
| Electron/Tauri | 100+ MB / 5 MB + webview | Node / webview | Still a browser engine underneath. |

Why curses:
- Zero new dependencies and almost zero disk. The project already requires `python3`, and curses ships with it.
- People practise in a real editor (nvim, nano, …) instead of a textarea. That suits the goal of rebuilding real coding skills.
- Reuses `trainer.py` as-is: `all_problems`, `check_lang`, `record_pass`, `progress.json`, `work/` layout.

If a windowed app is wanted later, a tkinter front end can be added on top of the same `trainer.py` functions. That needs Tcl/Tk installed (`python3.withPackages (p: [ p.tkinter ])` in nix).

## TUI design (`tui.py`, run with `python3 tui.py`)

```
┌ Coding Trainer ───────────────────── W4 · L4 · Day 1 · 2026-11-22 (today) ┐
│ W4 L4 Day 1 Graph traversal    │ P64 · Breadth-first search               │
│ > P64 bfs              ○○●○    │                                          │
│   P65 dfs components   ○○○○    │ Read an undirected graph, then a start   │
│   P66 islands          ○○○○    │ vertex s on the last line. ...           │
│ W3 L3 Day 7 Heaps              │                                          │
│   P61 heap sort        ●●●●    │ Sample input:                            │
│   ...                          │     6 6                                  │
│                                ├──────────────────────────────────────────┤
│                                │ py   PASS (5 tests)                      │
│                                │ c    WRONG on test 1 ...                 │
└ ↑↓ problem  ←→ lang [C]  e edit  c check  a check all  s solution  t theme  q quit ┘
```

- **Left pane:** unlocked days, newest first, with one ○/● per language (C, C++, Python, Rust). Today is highlighted.
- **Right top:** the problem statement. Markdown is shown plainly: `**bold**` becomes bold, backticks are stripped, code blocks are indented. It scrolls with PgUp/PgDn.
- **Right bottom:** checker output, the same text `check_lang` returns now.
- **Status bar:** the current language and the key hints.

Keys:

| Key | Action |
| --- | --- |
| `↑` `↓` / `j` `k` | select problem |
| `←` `→` / `1`–`4` | select language |
| `PgUp` `PgDn` | scroll statement |
| `e` | suspend the UI (`curses.endwin`), open `work/…/main.<lang>` in `$EDITOR` (creating it from the stub, plus `in.txt`, like `init`), redraw on return |
| `c` | check the selected language |
| `a` | check all four languages |
| `s` | show the reference solution in the output pane (only after the week ends, otherwise the unlock date) |
| `t` | cycle theme: System → Light → Dark |
| `q` | quit |

Theme (keeps the light/dark/system feature):
- **System** uses the terminal's own colours (`curses.use_default_colors()`, colour `-1`), so it follows whatever the terminal and OS are set to.
- **Light** and **Dark** use fixed curses colour pairs for background, text, muted text, accent, pass and fail.
- The choice is stored as `"theme"` in `progress.json`, so no extra file is needed.

Behaviour notes:
- Checks run synchronously. The output pane shows `Checking…` and refreshes when done; the slowest test takes a few seconds.
- The terminal must be at least 80×24. Below that, the UI shows a one-line "terminal too small" message.
- If no start date exists, the first screen offers "Press Enter to start today", like the web welcome screen.

## Disk-space reduction: generate large tests instead of storing them

Large tests (any `.in` over 100 KB) become small generator scripts:

```
problems/week3/p43_two_sum/tests/
  1.in  1.out  ...            small tests stay as files
  5.gen.py                    prints test 5's input (fixed random seed), ~10 lines
```

- At check time, `trainer.py` runs `5.gen.py` to get the input. It runs `solution.py` on that input to get the expected output, and caches both in `cache/` (gitignored). The first check of that problem takes a second longer, and later checks read the cache.
- The generators come from the existing scratch scripts (`gen_week2-4.py`), using the same seeds, so the tests stay identical. Each converted test is verified byte-for-byte against the current `.in`/`.out` before the old files are deleted.
- Result: test data goes from about 16.9 MB to about 1 MB in the working tree and in fresh clones of new history.
- `.git` keeps its current 12 MB, because the old large files stay in history. Shrinking it means rewriting history and force-pushing (`git filter-repo`). That is destructive, so it is listed as optional and needs your explicit go-ahead.

## Removing the browser UI

Once the TUI matches the web app (list, statement, edit, check, solution, theme), delete `app.py` and `static/`, and update the README. The CLI (`trainer.py`) stays as the scriptable interface.

## Steps (one commit each, pushed after each)

1. **`tui.py` skeleton:** layout, problem list, statement pane, navigation, quit.
2. **Edit and check:** `e` opens `$EDITOR`; `c` and `a` run checks; progress dots update.
3. **Solution, start screen, small-terminal message.**
4. **Themes:** System / Light / Dark, stored in `progress.json`.
5. **Generated large tests:** `*.gen.py`, the `cache/` folder, `.gitignore`, and byte-for-byte verification; then delete the 20 large `.in`/`.out` pairs.
6. **Remove the web UI:** delete `app.py` and `static/`; README and PLAN status update.
7. *(Optional, only with explicit approval)* rewrite git history to drop the old large test files, then force-push.

## How each step is tested

- **TUI:** run it in a real terminal through a pseudo-terminal (`script`/`tmux`) at 80×24 and at a larger size. Walk through select → edit (with `EDITOR` set to a scripted command) → check pass/fail → solution locked/unlocked → theme cycle → quit. Confirm `progress.json` and `work/` match what the CLI reports.
- **Generated tests:** for all 20, generator output equals the old `.in` and the cached expected output equals the old `.out`. All 84 reference solutions still pass `check`.
- **Size:** report `du -sh problems` before and after.

## Open questions

- Is a terminal UI acceptable, or is a separate window a must? A window means installing Tcl/Tk (~10–15 MB) for tkinter.
- Should git history be rewritten to reclaim the ~11 MB in `.git` (step 7)?
