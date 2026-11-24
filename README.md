This is a repo to create a software that will present problems with daily deliverables and submission checker.

For now the coding languages included are 
    - C
    - C++
    - Python
    - Rust

A new problem set is released every 3 days. The checker works any time after a set is released; the reference solutions of a set are released together with the next set.

The week just marks the levels of the problems with level (4 levels) 

It should be such that the problems should help someoen who is completly new to the coding world and should also help someone who want to revisit his coding skills as people are loosing the grip and undestanding due to use of coding agents 


## Usage

Requires `python3`, `gcc`, `g++` and `rustc`. No other dependencies.

### Menus and layout (desktop apps and web app)

| Menu | Item |
| --- | --- |
| **Course** | **Start at level ▸ 1–4**: that level's Set 1 is released today; lower levels stay locked; passed checks and saved code are kept · **Reset…** |
| **View** | **Problem list** (**Ctrl+B**) shows or hides the sidebar; the statement and editor take its space · **Theme ▸** System / Light / Dark |
| **Help** | **About** (version, link to this repository) |

- The ☰ button next to the title (or above the statement while the list is hidden) does the same as **Ctrl+B**.
- The welcome screen has a **Start at level** picker next to **Start today**.
- **Reset…** is a whole reset: after a confirmation (Cancel is the default) it deletes your progress, **all saved code in `work/`**, your settings and the test cache.
- The desktop apps keep the theme and problem-list state in `progress.json`; the web app keeps them in the browser.

### Hints

After a failed **Check**, the **Hint** button next to **Reference solution** lights up as `Hint 0/N`. Nothing is shown until you click it; each click adds one hint under the report.

- **Hint 1** describes your actual failure: the exception and its line, the crash signal, a timeout on a small or a large test, or what is off in your output (nothing printed, layout only, an extra or missing line, wrong sign, off by one, 32-bit overflow, wrong order, or the first differing value).
- **Hint 2** points toward the idea that fixes it on this problem, chosen by the test that failed. It never contains solution code.
- **Compile errors get no hints.** Reading compiler output is part of the training. Python syntax errors count as compile errors.
- A failure gets 1 or 2 hints: level-1 wrong answers, simple output problems and failures with no matching nudge get 1; the rest get 2.
- A new check, another language or another problem replaces the hints. Crashes are now reported as `RUNTIME ERROR` (they used to show as `WRONG`).

### Build system

```
make            # list targets
make run        # desktop app          make web        # web app
make install    # add to app grid      make uninstall  # remove from app grid
make test       # all 84 reference solutions + generators, in a temp copy
make dist       # test, then package the committed project as build/coding-trainer-<VERSION>.tar.gz
make clean      # remove build/, cache/, __pycache__/
```

The version lives in `VERSION`. No target touches your `work/` folder or `progress.json`.

### Windows

Install, and make sure each is on `PATH`:
- **Python 3** from python.org — includes the `py` / `pyw` launchers and tkinter, which the Windows window uses
- **gcc / g++** — MinGW-w64, e.g. from winlibs.com or MSYS2
- **Rust** via rustup (rustup.rs)
- **Git** — only for `build dist`

```
build              list targets
build run          desktop app (gui_tk.py, a tkinter replica of the GTK window)
build web          web app on http://localhost:8000
build install      add "Coding Trainer" (with icon) to the Start menu
build uninstall    remove it from the Start menu
build test         all 84 reference solutions + generators, in a temp copy
build dist         test, then package the committed project as build\coding-trainer-<VERSION>.zip
build clean        remove build\, cache\, __pycache__\
```

`build.cmd` runs `build.ps1` without changing PowerShell's execution policy. Set `PYTHON` / `GUI_PYTHON` to use other interpreters than `py` / `pyw`. No target touches `work\` or `progress.json`.

### Desktop app (native window)

```
./install-desktop.sh                  # once: adds "Coding Trainer" (with icon) to your app grid
./gui.py                              # or start it directly: /usr/bin/python3 gui.py
```

`install-desktop.sh` writes `~/.local/share/applications/coding-trainer.desktop` pointing at this folder (no root needed). Re-run it if you move the folder; remove the app with `rm ~/.local/share/applications/coding-trainer.desktop`.

A GTK 3 window with the same layout and menus as the web app: menu bar, collapsible sidebar with problem sets and progress dots, problem statement, C / C++ / Python / Rust editor tabs, **Check** and **Reference solution**. No browser or server needed. It uses the system Python because that is where GTK's Python bindings live (`python3-gi`, preinstalled on Ubuntu). It shares `work/` and `progress.json` with the CLI and web app.

### Web app

```
python3 app.py                        # then open http://localhost:8000
```

Sidebar shows the released problem sets with a dot per language (green = passed). Pick a problem, write code in the C / C++ / Python / Rust tabs, press **Check**. Code is saved to `work/` on every check, so the CLI and the app share the same files and progress.

Theme: **View ▸ Theme** — **System** follows your OS light/dark setting. The choice is remembered in the browser.

### CLI

```
python3 trainer.py start              # begin today at level 1 (or: start 2026-11-22 --level 3)
python3 trainer.py level 3            # restart the schedule at level 3 today; lower levels lock
python3 trainer.py reset              # delete progress, settings, ALL saved code and the cache (asks first)
python3 trainer.py list               # released problem sets + per-language progress
python3 trainer.py show P01           # read a problem
python3 trainer.py init P01           # creates work/week1/day01/p01_arithmetic/main.{c,cpp,py,rs} + in.txt
python3 trainer.py check P01          # compile + run all 4 against the tests (or: check P01 rs)
python3 trainer.py hint P01 py        # hint 1 for your current failure in Python (or: hint P01 py 2)
python3 trainer.py status             # weekly completion summary
python3 trainer.py solution P01       # reference solution, released with the next problem set
```

- Week W is level W (4 levels), 7 problem sets each. Starting at level L: set N of week W ≥ L is released on `start + 3*(7*(W-L) + N-1)` days, and its solutions 3 days later with the next set; weeks below L stay locked. Checking works any time after release.
- The sidebar and `list` mark the current set (released, solutions not out yet). `status` counts passes made before the solutions came out.
- Saved code lives in `work/weekW/dayNN/` (NN = set number; the folder name is kept from the old daily sets).
- Your progress is saved in `progress.json`.

## Adding a week

```
problems/weekN/
  week.json                  {"title": ..., "level": N, "sets": [{"title": ..., "problems": ["p22_name", ...]}, ...]}
  p22_name/
    problem.md               statement
    solution.py              reference solution (shown with the next problem set)
    tests/1.in, 1.out, ...   test 1 is the sample copied to in.txt
    tests/5.gen.py           large test: prints its input (fixed random seed)
    hints.json               hint 2 per failed test: {"tests": {"3": ...}, "timeout": ..., "runtime": ..., "wrong": ..., "hints": 1|2}
```

Large tests are not stored. `N.gen.py` prints the input and the reference solution produces the expected output; both are generated on the first check and cached in `cache/` (gitignored, ~16 MB once every problem has been checked).
