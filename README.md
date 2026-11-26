This is a repo to create a software that will present problems with daily deliverables and submission checker.

For now the coding languages included are 
    - C
    - C++
    - Python
    - Rust

A new problem set is released every 3 days. The checker works any time after a set is released; the reference solutions of a set are released together with the next set.

The week just marks the levels of the problems with level (4 levels) 

It should be such that the problems should help someoen who is completly new to the coding world and should also help someone who want to revisit his coding skills as people are loosing the grip and undestanding due to use of coding agents 

For complete beginners there is also the **Proficiency capsule**: 150 small questions from `Hello, World!` to proficient, with no schedule. See [Proficiency capsule](#proficiency-capsule).


## Usage

Requires `python3`, `gcc`, `g++` and `rustc`. No other dependencies.

### Project layout

```
coding_trainer/
├── README.md  VERSION  Makefile  build.cmd     entry points: `make <target>` (Linux), `build <target>` (Windows)
├── src/                                        the program
│   ├── trainer.py                              CLI and checker (used by all the UIs)
│   ├── gui.py                                  GTK desktop window (Linux)
│   ├── gui_tk.py                               tkinter desktop window (Windows)
│   ├── app.py                                  web app
│   └── static/index.html                       web app page
├── problems/week1..week4/                      problems, tests, hints, reference solutions
├── problems/capsule/                           the Proficiency capsule: 150 questions, solutions in all 4 languages
├── assets/                                     app icons (svg, png, ico)
├── scripts/                                    build.ps1 (Windows build), install-desktop.sh, selftest.py
├── docs/                                       plans and notes (not shipped by `dist`)
└── build/                                      `dist` output (gitignored)
```

### Your data

Your progress, settings, saved code and the test cache live outside the program folder, so the program can be replaced by a new version or installed in a read-only place:

| OS | Folder |
| --- | --- |
| Linux | `~/.local/share/coding-trainer/` |
| Windows | `%APPDATA%\coding-trainer\` |

It holds `progress.json` (course and capsule progress), `work/` (your code; capsule code in `work/capsule/<language>/`) and `cache/` (generated large tests). The CLI, desktop apps and web app all share it.

### Building on another machine

1. Install the compilers and Python (see **Windows** below for the Windows list; on Ubuntu: `sudo apt install python3 gcc g++` and Rust via rustup, then `rustup default stable`).
2. Get the program: `git clone` this repository, or copy `build/coding-trainer-<VERSION>.tar.gz` / `.zip` made by `make dist` / `build dist` and extract it anywhere.
3. In that folder: `make test` (or `build test`) to check the toolchain, then `make install` (or `build install`) to add it to the app grid / Start menu.

### Menus and layout (desktop apps and web app)

| Menu | Item |
| --- | --- |
| **Course** | **Start at level ▸ 1–4**: that level's Set 1 is released today; lower levels stay locked; passed checks and saved code are kept · **Reset…** |
| **View** | **Problem list** (**Ctrl+B**) shows or hides the sidebar; the statement and editor take its space · **Theme ▸** System / Light / Dark |
| **Help** | **About** (version, link to this repository) |

- **◉ Proficiency** at the right end of the menu bar (in the tkinter window: the row just under it) opens the [Proficiency capsule](#proficiency-capsule); click it again to return to the course.
- The ☰ button next to the title (or above the statement while the list is hidden) does the same as **Ctrl+B**.
- The welcome screen has a **Start at level** picker next to **Start today**.
- **Reset…** is a whole reset: after a confirmation (Cancel is the default) it deletes your progress, **all saved code in `work/`**, your settings and the test cache (everything in [your data folder](#your-data)).
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
make test       # all 84 reference solutions + 150 capsule questions in 4 languages + generators, in a temp copy
make dist       # test, then package the committed app (no docs/) as build/coding-trainer-<VERSION>.tar.gz
make clean      # remove build/, src/__pycache__/ and the test cache
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
build run          desktop app (src\gui_tk.py, a tkinter replica of the GTK window)
build web          web app on http://localhost:8000
build install      add "Coding Trainer" (with icon) to the Start menu
build uninstall    remove it from the Start menu
build test         all 84 reference solutions + 150 capsule questions in 4 languages + generators, in a temp copy
build dist         test, then package the committed app (no docs\) as build\coding-trainer-<VERSION>.zip
build clean        remove build\, src\__pycache__\ and the test cache
```

`build.cmd` runs `scripts\build.ps1` without changing PowerShell's execution policy. Set `PYTHON` / `GUI_PYTHON` to use other interpreters than `py` / `pyw`. No target touches `work\` or `progress.json`.

### Desktop app (native window)

```
scripts/install-desktop.sh            # once: adds "Coding Trainer" (with icon) to your app grid (same as make install)
src/gui.py                            # or start it directly: /usr/bin/python3 src/gui.py
```

`scripts/install-desktop.sh` writes `~/.local/share/applications/coding-trainer.desktop` pointing at this folder (no root needed). Re-run it if you move the folder; remove the app with `rm ~/.local/share/applications/coding-trainer.desktop`.

A GTK 3 window with the same layout and menus as the web app: menu bar, collapsible sidebar with problem sets and progress dots, problem statement, C / C++ / Python / Rust editor tabs, **Check** and **Reference solution**. No browser or server needed. It uses the system Python because that is where GTK's Python bindings live (`python3-gi`, preinstalled on Ubuntu). It shares [your data folder](#your-data) with the CLI and web app.

### Web app

```
python3 src/app.py                    # then open http://localhost:8000
```

Sidebar shows the released problem sets with a dot per language (green = passed). Pick a problem, write code in the C / C++ / Python / Rust tabs, press **Check**. Code is saved to `work/` in [your data folder](#your-data) on every check, so the CLI and the app share the same files and progress.

Theme: **View ▸ Theme** — **System** follows your OS light/dark setting. The choice is remembered in the browser.

### CLI

```
python3 src/trainer.py start          # begin today at level 1 (or: start 2026-11-22 --level 3)
python3 src/trainer.py level 3        # restart the schedule at level 3 today; lower levels lock
python3 src/trainer.py reset          # delete progress, settings, ALL saved code and the cache (asks first)
python3 src/trainer.py list           # released problem sets + per-language progress
python3 src/trainer.py show P01       # read a problem
python3 src/trainer.py init P01       # creates work/week1/day01/p01_arithmetic/main.{c,cpp,py,rs} + in.txt
python3 src/trainer.py check P01      # compile + run all 4 against the tests (or: check P01 rs)
python3 src/trainer.py hint P01 py    # hint 1 for your current failure in Python (or: hint P01 py 2)
python3 src/trainer.py status         # weekly completion summary
python3 src/trainer.py solution P01   # reference solution, released with the next problem set
```

```
python3 src/trainer.py capsule py           # capsule modules and progress in one language (c, cpp, py, rs)
python3 src/trainer.py capsule show C001 py # a question, with its Learn section for that language
python3 src/trainer.py capsule init C001 py # creates work/capsule/py/c001_hello_world/main.py + in.txt
python3 src/trainer.py capsule check C001 py
python3 src/trainer.py capsule hint C001 py # (or: hint C001 py 2)
python3 src/trainer.py capsule solution C001 py   # after your first check of C001 in py
```

The `capsule` commands work without `start`.

- Week W is level W (4 levels), 2 problem sets each (10 and 11 problems). Starting at level L: set N of week W ≥ L is released on `start + 3*(2*(W-L) + N-1)` days, and its solutions 3 days later with the next set; weeks below L stay locked. Checking works any time after release.
- The sidebar and `list` mark the current set (released, solutions not out yet). `status` counts passes made before the solutions came out.
- Saved code lives in `work/weekW/dayNN/` in [your data folder](#your-data) (NN = set number; the folder name is kept from the old daily sets).
- Your progress is saved in `progress.json` in [your data folder](#your-data).

## Proficiency capsule

150 short questions in 15 modules of 10, from printing `Hello, World!` to small real programs. Each module ends with a checkpoint question that combines its ideas.

| Module | Questions | Module | Questions |
| --- | --- | --- | --- |
| 1 Hello, output | C001–C010 | 9 Strings | C081–C090 |
| 2 Variables and input | C011–C020 | 10 2D arrays | C091–C100 |
| 3 Arithmetic and types | C021–C030 | 11 Recursion | C101–C110 |
| 4 Conditionals | C031–C040 | 12 Structs and records | C111–C120 |
| 5 Loops | C041–C050 | 13 Sorting and searching | C121–C130 |
| 6 Nested loops and patterns | C051–C060 | 14 Hash maps and sets | C131–C140 |
| 7 Functions | C061–C070 | 15 Putting it together | C141–C150 |
| 8 Arrays and lists | C071–C080 | | |

- **One capsule per language.** C, C++, Python and Rust each have their own copy of the same 150 questions, with separate progress. Pick the language at the top of the capsule's sidebar; the editor then shows only that language. The button reads `◉ Proficiency · Python 37/150`.
- **One question at a time.** Only C001 is open at first; passing a question opens the next one in the same language. The sidebar marks each question ✓ passed, ▶ open or 🔒 locked.
- **Learn sections.** The first question that uses a new piece of syntax starts with a short **Learn** part showing it in your language, on a different example than the task.
- **Instant check, hints** as in the course. A few questions have a large generated test that only a fast enough method passes.
- **Solution after an attempt.** **Reference solution** is enabled once you have checked the question at least once in that language (pass or fail); it shows the solution in that language. **Next →** opens the next question after a pass.
- No schedule and no start date: the capsule works before (and without) starting the course. **Reset…** clears capsule progress too.

### Adding capsule questions

```
problems/capsule/
  capsule.json               {"title": "Proficiency", "modules": [{"title": ..., "problems": ["c001_hello_world", ...]}, ...]}
  c001_hello_world/
    problem.md               statement, the same for every language
    learn.c.md, learn.cpp.md, learn.py.md, learn.rs.md   optional Learn section per language, shown above the task
    solution.c, solution.cpp, solution.py, solution.rs   reference solutions; solution.py also produces the expected output of N.gen.py tests
    tests/1.in, 1.out, ...   as for the course (test 1 is the sample in in.txt); N.gen.py for large tests
    hints.json               optional, as for the course
```

Questions are chained in the order of `capsule.json`. `make test` runs all four solutions of every question.

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

Large tests are not stored. `N.gen.py` prints the input and the reference solution produces the expected output; both are generated on the first check and cached in `cache/` in [your data folder](#your-data) (~16 MB once every problem has been checked).
