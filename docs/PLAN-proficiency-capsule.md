# PLAN: Proficiency capsule — 150 questions from Hello World to proficient

## Goal

Add a **Proficiency** capsule (a pill-shaped button) to the top ribbon. Clicking it switches the app to a separate track of **150 short questions** that take a complete beginner from printing `Hello, World!` to writing small real programs on their own.

Unlike the course:

- **No schedule.** Every question is open from the first launch, even before the course is started.
- **Instant check.** The same checker as the course (`check_lang`, hints included).
- **Instant solution.** The reference solution can be opened at any time, in the language of the current tab.
- **Small steps.** Each question teaches or practises one idea. A module ends with a checkpoint question that combines the module's ideas.

This applies to all four front ends, which share `trainer.py`: GTK (`gui.py`), tkinter (`gui_tk.py`), web (`app.py` + `static/index.html`) and the CLI.

## Why 150

- 15 modules × 10 questions. 10 is enough to go from "first time seeing it" to "can use it without thinking" for one idea, with a checkpoint at the end.
- At 10–20 minutes a question that is about 25–50 hours: a few weeks of daily practice. Fewer than ~100 skips steps a beginner needs; more than ~200 turns into the course, which already covers the harder problems.
- After the capsule the learner is ready for the course at level 1–2.

## Layout

```
┌ menu bar ─────────────────────────────────────────────────────────────┐
│ Course  View  Help                          ( ◉ Proficiency  37/150 ) │
├───────────────────────────────────────────────────────────────────────┤
│ ☰ Proficiency          │ C038 · Sum of a list                         │
│ ▸ 1 Hello, output  10/10│ ...statement...                             │
│ ▸ 2 Variables, input  …│                                              │
│ ▾ 4 Conditionals   7/10│ [C] [C++] [Python] [Rust]                    │
│   C031 Max of two  ●○○●│ ...editor...                                 │
│   C032 ...             │ [Check] [Solution] [Hint 0/2] [Next →]       │
│   ...                  │ ...result...                                 │
└───────────────────────────────────────────────────────────────────────┘
```

**Capsule button** (right end of the menu bar)
- Label `◉ Proficiency  N/150`, where N is the number of questions passed in at least one language.
- Click: switches the sidebar and the main pane to the capsule. The button turns accent-coloured while the capsule is open.
- Click again (or pick a course problem from **Course**): back to the course, on the problem that was open before.
- Shown on the welcome screen too, so a new user can go straight to the capsule without starting the course.

**Capsule mode**
- Sidebar: the 15 modules, each with `passed/10`, expandable to its questions with the four language dots (same dots as the course). The module with the first unpassed question is expanded and marked as "next up".
- **Solution** button: always enabled. Shows `solution.<lang>` for the current tab under the result. No "unlocks on" note.
- **Next →** button: enabled after a pass; opens the next question in order.
- Hints, Check, editor tabs and the result pane are exactly the course's.

## Curriculum

Every question names its idea in the statement's **Focus** line. The first question that uses a new piece of syntax starts with a **Learn** section: a few lines showing that syntax in all four languages, on a different example than the task, so it teaches without giving the answer away.

| # | Module | Questions (C001–C150) | Checkpoint |
| --- | --- | --- | --- |
| 1 | Hello, output | print a line, several lines, quotes and escapes, a blank line, print without newline, print numbers, print an expression | ASCII name banner |
| 2 | Variables and input | read an int, two ints, a word, a whole line, swap, constants, reassign, echo input | "Hello, <name>! You are <age>." |
| 3 | Arithmetic and types | + − × ÷, integer vs float division, modulo, rounding, casting, 64-bit overflow, precedence | seconds → h:m:s |
| 4 | Conditionals | if / else, else-if chains, max of two / three, even/odd, ranges, `and` / `or`, nested if | grade calculator |
| 5 | Loops | count to n, while, sum 1..n, factorials, digits of a number, break / continue, read until 0 | number guessing (from input) |
| 6 | Nested loops and patterns | rectangle, triangle, pyramid, multiplication table, number grid, checkerboard | diamond |
| 7 | Functions | define and call, parameters, return, several functions, pure vs printing, early return | prime checker used by a primes-in-range |
| 8 | Arrays / lists | read n values, sum / min / max, reverse, count matches, shift, prefix sums, second largest | running average |
| 9 | Strings | length, index a char, reverse, case change, count vowels, split words, join, palindrome | word statistics |
| 10 | 2D arrays | read a grid, row / column sums, transpose, diagonal, neighbours, find in grid | tic-tac-toe winner |
| 11 | Recursion | factorial, Fibonacci, power, sum of digits, string reverse, binary strings, subsets | permutations |
| 12 | Structs / records | point, distance, student record, array of records, sort by field, update by id | inventory report |
| 13 | Sorting and searching | linear search, bubble, insertion, built-in sort, custom key, binary search, two pointers | merge two sorted lists |
| 14 | Hash maps and sets | count words, unique values, first repeat, two-sum, group anagrams, set ops | most frequent element |
| 15 | Putting it together | stack (brackets), queue (simulation), greedy (coins), simple DP (stairs), parsing input, a large test (fast enough) | mini text-adventure state machine |

The exact question list for each module is written in `problems/capsule/capsule.json` as the module is built (see **Steps**).

## Data

```
problems/capsule/
  capsule.json               {"title": "Proficiency", "modules": [{"title": ..., "problems": ["c001_hello", ...]}, ...]}
  c001_hello/
    problem.md               statement (with Learn section where it introduces syntax)
    solution.py              reference solution; also produces the expected output of .gen.py tests
    solution.c  .cpp  .rs    reference solutions shown in the other tabs
    tests/1.in, 1.out, ...   same format as the course; test 1 is the sample in in.txt
    hints.json               same format as the course
```

- IDs are `c001`–`c150`, so they never clash with the course's `p01`… IDs.
- Passes go into `progress["passed"]` like course passes (the IDs are unique). **Reset…** clears them with everything else.
- Saved code: `work/capsule/c001_hello/main.{c,cpp,py,rs}` in the data folder.
- Questions that print without reading input have an empty `1.in`.

## Code changes

**`trainer.py`**
- `CAPSULE = PROBLEMS / "capsule"`.
- `capsule_problems()` yields the same dicts as `all_problems`, with `unlock` and `solution_unlock` = `datetime.date.min`, `"module"` and `"module_title"` instead of week/set, and `work = WORK / "capsule" / name`.
- `find_problem` also searches `capsule_problems()`, and works without a started course for `c` IDs.
- `solution_text(p, lang)` returns `solution.<lang>` (course problems keep `solution.py`).
- CLI: `capsule` command lists modules and progress. `show`, `init`, `check`, `hint`, `solution C012 [lang]` accept capsule IDs.
- `weeks()` keeps globbing `week*` only, so the course does not change.

**`app.py` + `static/index.html`**
- `GET /api/capsule`: modules with each question's passed languages.
- `/api/problem/<id>` returns `solution` per language for capsule problems.
- Capsule button in `#menubar` (right-aligned, pill style with the theme's accent), capsule sidebar, **Next →** button.

**`gui.py` / `gui_tk.py`**
- Same button on the right of the menu bar (GTK: a `Gtk.Button` packed after the `Gtk.MenuBar`; tk: a button in the menu row frame).
- Sidebar switches between course sets and capsule modules. Solution button and **Next →** as in the web app.

**`scripts/selftest.py`**
- Runs all four capsule solutions per question against its tests (the course only checks `solution.py`). `make test` counts go from 84 to 84 + 600.

## Steps (each one a commit, pushed)

1. Engine: `capsule.json`, `capsule_problems`, `find_problem`, `solution_text`, CLI `capsule` command, with module 1 (C001–C010) as real content.
2. Selftest runs capsule solutions in all four languages.
3. Web app: capsule button, sidebar, Solution per language, Next →.
4. GTK app: same.
5. tkinter app: same.
6. Modules 2–5 (C011–C050).
7. Modules 6–10 (C051–C100).
8. Modules 11–15 (C101–C150).
9. README: capsule section, CLI commands, `problems/capsule/` format; bump `VERSION`.

## Open questions

- **Locking:** all 150 open (planned), or each question opens only after the previous one is passed?
- **What counts as passed:** one language (planned, since a beginner usually learns one), or all four like the course's dots?
- **Solution timing:** always visible (planned, "instant solutions"), or only after the first Check attempt so the learner tries first?
