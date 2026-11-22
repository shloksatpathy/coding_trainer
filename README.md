This is a repo to create a software that will present problems with daily deliverables and submission checker.

For now the coding languages included are 
    - C
    - C++
    - Python
    - Rust

Each week presents a set of problems with daily submission the problems checker works always but the solution is provided only at the end of the problem set that is at the end of the week

The week just marks the levels of the problems with level (4 levels) 

It should be such that the problems should help someoen who is completly new to the coding world and should also help someone who want to revisit his coding skills as people are loosing the grip and undestanding due to use of coding agents 


## Usage

Requires `python3`, `gcc`, `g++` and `rustc`. No other dependencies.

### Desktop app (native window)

```
./gui.py                              # or: /usr/bin/python3 gui.py
```

A GTK 3 window with the same layout as the web app: sidebar with days and progress dots, problem statement, C / C++ / Python / Rust editor tabs, **Check**, **Reference solution**, and the System / Light / Dark theme selector. No browser or server needed. It uses the system Python because that is where GTK's Python bindings live (`python3-gi`, preinstalled on Ubuntu). It shares `work/` and `progress.json` with the CLI and web app; the theme choice is stored in `progress.json`.

### Web app

```
python3 app.py                        # then open http://localhost:8000
```

Sidebar shows the unlocked days with a dot per language (green = passed). Pick a problem, write code in the C / C++ / Python / Rust tabs, press **Check**. Code is saved to `work/` on every check, so the CLI and the app share the same files and progress.

Theme: pick **System** (follows your OS light/dark setting), **Light** or **Dark** at the top of the sidebar. The choice is remembered in the browser.

### CLI

```
python3 trainer.py start              # begin today (or: start 2026-11-22)
python3 trainer.py list               # unlocked days + per-language progress
python3 trainer.py show P01           # read a problem
python3 trainer.py init P01           # creates work/week1/day01/p01_arithmetic/main.{c,cpp,py,rs} + in.txt
python3 trainer.py check P01          # compile + run all 4 against the tests (or: check P01 rs)
python3 trainer.py status             # weekly completion summary
python3 trainer.py solution P01       # reference solution, only after the week ends
```

- Day N of week W unlocks on `start + 7*(W-1) + (N-1)` days. Checking works any time after unlock.
- Week W is level W (4 levels).
- Your progress is saved in `progress.json`.

## Adding a week

```
problems/weekN/
  week.json                  {"title": ..., "level": N, "days": [{"title": ..., "problems": ["p22_name", ...]}, ...]}
  p22_name/
    problem.md               statement
    solution.py              reference solution (shown after the week ends)
    tests/1.in, 1.out, ...   test 1 is the sample copied to in.txt
```
