# PLAN: Proficiency capsule — 150 questions from Hello World to proficient — done

Status (v0.3.0): all 9 steps are in. C, C++ and Python reference solutions of all 150 questions pass their tests (`make test`). The Rust solutions are written but were not compiled on the build machine (no Rust toolchain there), and the tkinter window was checked statically only (no tkinter there).

## Goal

Add a **Proficiency** capsule (a pill-shaped button) to the top ribbon. Clicking it switches the app to a separate track of **150 short questions** that take a complete beginner from printing `Hello, World!` to writing small real programs on their own.

Unlike the course:

- **No schedule, a chain instead.** Question N opens as soon as question N−1 is passed. Only C001 is open at first, even before the course is started.
- **One set per language.** C, C++, Python and Rust each have their own capsule: the same 150 questions, with separate progress and separate locks. Passing C012 in Python opens C013 in Python only.
- **Instant check.** The same checker as the course (`check_lang`, hints included).
- **Solution after an attempt.** The **Solution** button is enabled once the learner has run at least one Check on that question in that language. The solution is shown only when the button is clicked, and only in that language.
- **Small steps.** Each question teaches or practises one idea. A module ends with a checkpoint question that combines the module's ideas.

This applies to all four front ends, which share `trainer.py`: GTK (`gui.py`), tkinter (`gui_tk.py`), web (`app.py` + `static/index.html`) and the CLI.

## Why 150

- 15 modules × 10 questions. 10 is enough to go from "first time seeing it" to "can use it without thinking" for one idea, with a checkpoint at the end.
- At 10–20 minutes a question that is about 25–50 hours: a few weeks of daily practice. Fewer than ~100 skips steps a beginner needs; more than ~200 turns into the course, which already covers the harder problems.
- After the capsule the learner is ready for the course at level 1–2.

## Layout

```
┌ menu bar ─────────────────────────────────────────────────────────────────┐
│ Course  View  Help                       ( ◉ Proficiency · Python 37/150 ) │
├───────────────────────────────────────────────────────────────────────────┤
│ ☰ Proficiency [Python ▾] │ C038 · Sum of a list                           │
│ ✓ 1 Hello, output  10/10 │ Learn (Python) …                               │
│ ✓ 2 Variables, input 10/10│ ...statement...                               │
│ ▾ 4 Conditionals   7/10  │ Python                                         │
│   ✓ C031 Max of two      │ ...editor...                                   │
│   ▶ C038 Sum of a list   │                                                │
│   🔒 C039 ...            │ [Check] [Solution] [Hint 0/2] [Next →]         │
│ 🔒 5 Loops          0/10 │ ...result...                                   │
└───────────────────────────────────────────────────────────────────────────┘
```

**Capsule button** (right end of the menu bar)
- Label `◉ Proficiency · <language>  N/150`, where N is the number of questions passed in the selected language.
- Click: switches the sidebar and the main pane to the capsule, on the first unpassed question of the selected language. The button turns accent-coloured while the capsule is open.
- Click again (or start a level from **Course**): back to the course, on the problem that was open before.
- Shown on the welcome screen too, so a new user can go straight to the capsule without starting the course.

**Capsule mode**
- **Language picker** at the top of the sidebar (C / C++ / Python / Rust). It picks which of the four capsules is shown. The last choice is remembered in the settings.
- Editor: only the selected language (no C / C++ / Python / Rust tabs), since each capsule is one language.
- Sidebar: the 15 modules with `passed/10`. Each question is ✓ passed, ▶ open (the next one to do) or 🔒 locked. A module opens with its first question. Locked questions can't be opened.
- **Check**: as in the course. A pass marks the question ✓ and opens the next one.
- **Solution** button: disabled until the first Check on this question in this language (pass or fail). After that it stays enabled, also after a restart. Clicking it shows `solution.<lang>` under the result. Nothing is shown until it is clicked.
- **Next →** button: enabled after a pass; opens the next question.
- Hints and the result pane are exactly the course's.

## Curriculum

Every question names its idea in the statement's **Focus** line. The first question that uses a new piece of syntax has a **Learn** section, shown above the statement: a few lines showing that syntax in the capsule's language, on a different example than the task, so it teaches without giving the answer away.

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
    problem.md               statement, the same for all four languages
    learn.c.md  learn.cpp.md  learn.py.md  learn.rs.md
                             Learn section per language (only on questions that introduce syntax)
    solution.c  solution.cpp  solution.py  solution.rs
                             reference solution per language; solution.py also produces the expected output of .gen.py tests
    tests/1.in, 1.out, ...   same format as the course; test 1 is the sample in in.txt
    hints.json               same format as the course
```

- IDs are `c001`–`c150`, so they never clash with the course's `p01`… IDs.
- Progress in `progress.json`, kept apart from the course:
  ```json
  "capsule": {
    "lang": "py",
    "passed":    {"py": {"c001": "2026-11-25", "c002": "2026-11-25"}, "rs": {"c001": "2026-11-26"}},
    "attempted": {"py": ["c001", "c002", "c003"], "rs": ["c001"]}
  }
  ```
  Question N is open in a language when N = 1 or question N−1 is in `passed[lang]`. **Reset…** clears it with everything else.
- Saved code: `work/capsule/<lang>/c001_hello/main.<lang>` in the data folder, one folder per capsule.
- Questions that print without reading input have an empty `1.in`.

## Code changes

**`trainer.py`**
- `CAPSULE = PROBLEMS / "capsule"`.
- `capsule_problems()`: a list of dicts with `id`, `name`, `dir`, `module`, `module_title`, in order.
- `capsule_open(progress, lang, p)`: true for the first question or when the previous one is passed in `lang`.
- `capsule_check(progress, p, lang)`: refuses a locked question, otherwise runs `check_lang` with `work/capsule/<lang>/`, adds `p` to `attempted[lang]` and, on a pass, to `passed[lang]`.
- `capsule_solution(progress, p, lang)`: refuses until `p` is in `attempted[lang]`, then returns `solution.<lang>`.
- CLI: `capsule [lang]` lists modules and progress for one language. `capsule show|init|check|hint|solution C012 <lang>` act on one question in one capsule. The course commands don't change.

**`app.py` + `static/index.html`**
- `GET /api/capsule?lang=py`: modules with each question's state (passed / open / locked) and whether it was attempted.
- `GET /api/capsule/problem/<id>?lang=py`: statement, Learn section and saved code; no solution.
- `POST /api/capsule/check`, `POST /api/capsule/solution` (refused before the first attempt).
- Capsule button in `#menubar` (right-aligned, pill style with the theme's accent), language picker, capsule sidebar, **Next →** button.

**`gui.py` / `gui_tk.py`**
- Same button on the right of the menu bar (GTK: a `Gtk.Button` packed after the `Gtk.MenuBar`; tk: a button in the menu row frame).
- Sidebar switches between course sets and the capsule. Language picker, single-language editor, Solution and **Next →** as in the web app.

**`scripts/selftest.py`**
- Runs all four capsule solutions per question against its tests (the course only checks `solution.py`). `make test` goes from 84 to 84 + 600 solutions.

## Steps (each one a commit, pushed)

1. Engine: `capsule.json`, `capsule_problems`, locking, attempts, `capsule_check`, `capsule_solution`, CLI `capsule` commands, with module 1 (C001–C010) as real content in all four languages.
2. Selftest runs capsule solutions in all four languages.
3. Web app: capsule button, language picker, sidebar with locks, Solution after an attempt, Next →.
4. GTK app: same.
5. tkinter app: same.
6. Modules 2–5 (C011–C050).
7. Modules 6–10 (C051–C100).
8. Modules 11–15 (C101–C150).
9. README: capsule section, CLI commands, `problems/capsule/` format; bump `VERSION`.

## Decisions

- **Locking:** each question opens once the previous one is passed.
- **Languages:** a separate capsule per language with the same questions; progress and locks are per language.
- **Solution:** the button is enabled after at least one Check on that question in that language; the solution is shown only when it is clicked.
