# PLAN: own window, fully local, minimal disk use

## Goal

Give the trainer its own window (no browser, no local web server) that replicates the web interface, and cut the project's disk footprint.

## Where we are (measured 2026-11-22)

| Item | Size / state |
| --- | --- |
| `trainer.py` (CLI + checker) | 246 lines, stdlib only |
| `app.py` + `static/index.html` (web UI) | 287 lines, needs a browser + local HTTP server |
| `problems/` | 1,022 files, 17 MB → **947 KB with generated tests** |
| └ 20 large test inputs and their outputs | **15.9 MB of the 16.9 MB of test data** |
| `.git` | 12 MB (history already contains the large tests) → **748 KB after the rewrite** |
| Python | nix 3.13: no GUI toolkit · system 3.12 (`/usr/bin/python3`): GTK 3.24 via `python3-gi` ✅ |
| Toolchains | gcc/g++ 15.3 ✅, rustc ⚠️ (`rustup default stable` not run yet) |
| Editor | `$EDITOR=nvim` |

## Decision: native GTK 3 window (`gui.py`) — done

The choice was a windowed replica of the web interface rather than a terminal UI.

| Option | Extra disk | New dependencies | Notes |
| --- | --- | --- | --- |
| **GTK 3 via system Python (chosen)** | **~20 KB (one file)** | **none — `python3-gi` + GTK 3.24 are preinstalled on Ubuntu 24.04** | Real window, styled with CSS to match the web app. |
| tkinter | ~10–15 MB Tcl/Tk | Tk for the nix Python | Not installed. |
| Native Rust GUI (egui/iced) | 5–10 MB binary, ~0.5–1 GB `target/` while building | Rust crates | Most work, biggest build footprint. |
| Electron/Tauri | 100+ MB / 5 MB + webview | Node / webview | Still a browser engine underneath. |

What `gui.py` replicates from the web app:
- Sidebar: unlocked days (newest at the bottom, scrolled to today), one dot per language, green when passed.
- Statement pane: markdown shown with bold, inline code and code blocks.
- Editor: C / C++ / Python / Rust tabs, Tab inserts 4 spaces, per-language text kept while switching.
- **Check** saves to `work/` and runs the tests in a background thread (the window stays responsive), then shows PASS or the input / expected / got diff.
- **Reference solution** is enabled only after the week ends; otherwise the unlock date is shown.
- Theme selector: System (follows the GNOME `color-scheme` setting live), Light, Dark — the same palettes as the web app, stored in `progress.json`.
- Welcome screen with **Start today** when there is no progress yet.

Tested by driving the real widgets from a script and rendering offscreen: Python pass, C wrong answer, solution locked/unlocked, all three themes, welcome → start, progress dots and saved files.

The web app (`app.py`, `static/`) stays as a separate option.

## Disk-space reduction: generate large tests instead of storing them — done

Large tests (input or output over 100 KB) become small generator scripts:

```
problems/week3/p43_two_sum/tests/
  1.in  1.out  ...            small tests stay as files
  5.gen.py                    prints test 5's input (fixed random seed), ~10 lines
```

- At check time, `trainer.py` runs `5.gen.py` to get the input. It runs `solution.py` on that input to get the expected output, and caches both in `cache/` (gitignored). The first check of that problem takes a second longer, and later checks read the cache.
- Byte-for-byte reproduction of the old files was not possible: they were drawn from one random sequence shared by a whole week. Each generator has its own fixed seed and the same shape as the test it replaces (identical line and token counts, same value ranges).
- Verified: every generator prints identical output on repeated runs and on both Pythons (nix 3.13 and system 3.12); all 84 reference solutions pass `check` with the same test counts as before; a cached re-check takes ~0.2 s.
- P39's large test was random, so the naive O(n²) solution passed it. Its generator is now worst-case (a long descending run), and the naive solution times out as the statement says.
- Result: `problems/` went from 17 MB to 947 KB. `cache/` holds ~16 MB, but only on machines that run the checks, and it is never committed.
- History rewritten (approved 2026-11-22) with `git filter-branch` to drop the 42 old files from every commit, then force-pushed. Same 18 commits, identical final tree; `.git` went from 16 MB to 748 KB and the largest blob in history is now ~100 KB. A backup of the pre-rewrite repo is in `../coding_trainer-backup-2026-11-22.bundle`.

## Steps (one commit each, pushed after each)

1. ✅ **Native window `gui.py`:** replica of the web interface (see above).
2. ✅ **Generated large tests:** 21 `*.gen.py` scripts replace 42 large `.in`/`.out` files; `cache/` is gitignored.
3. ✅ **History rewrite:** old large test files removed from all commits; force-pushed.
