# PLAN: on-demand hints based on the learner's actual error — done

## Goal

Add a **Hint** button to the action row, next to **Check** and **Reference solution**. It works like this:

- **Nothing is shown until the learner asks.** A failed Check doesn't reveal any hint. The button only lights up.
- Each failure has **1 or 2 hints**. How many depends on the kind of error and the problem's difficulty.
- The hints are **about this failure**. They are built from what went wrong in the learner's code: which exception, which test, which output line differed. They are not a general tip for the problem.
- **Compile errors get no hints.** Reading compiler output is a skill the learner has to build, so the trainer never explains or rephrases it. After a compile error the Hint button stays disabled.

This applies to all four front ends, which share `trainer.py`: GTK (`gui.py`), tkinter (`gui_tk.py`), web (`app.py` + `static/index.html`) and the CLI.

## Where things are today (v0.2.0)

- `trainer.check_lang(p, lang)` returns `(ok, report)`, where `report` is a formatted string. The UIs print it in the result pane.
- It reports four outcomes: `missing`, `COMPILE ERROR` (compiler stderr), `TIMEOUT on test N`, and `WRONG on test N` (input, expected and got).
- **A runtime error is not reported as its own outcome.** A crash (Python traceback, segfault, Rust panic) shows up as `WRONG` with stderr glued onto the output. Its exit code is ignored.
- The action row is `[Check] [Reference solution] <label id=hint>`. That label already exists, but it only says "Solution unlocks …". It will be renamed `solution_note` so that "hint" means only the new feature.
- Each test targets one edge case. For example, P01's tests are `-7 2`, `7 2`, `7 -2`, `-9 -4`, `10 5`, `0 3`, which cover the signs and zero. Large tests are `N.gen.py`. So **the test that failed already says a lot about the mistake**, and the plan builds on that.

## Design

### Layout

```
┌ editor ───────────────────────────────────────────────────────────┐
│ [C] [C++] [Python] [Rust]                                         │
│ ...                                                               │
│ [Check] [Reference solution] [💡 Hint 0/2]   Solution unlocks …   │
├───────────────────────────────────────────────────────────────────┤
│ py   WRONG on test 3                                              │
│ input: 7 -2   expected: 5 9 -14 -3 1   got: 5 9 -14 -4 -1         │
│ ── Hint 1/2 ──────────────────────────────────────────────────    │
│ Values 4 and 5 are wrong: you printed -4 and -1, expected -3      │
│ and 1. The other values are right.                                │
└───────────────────────────────────────────────────────────────────┘
```

**Hint button**
- **Disabled** before any Check, after a PASS, after a compile error, and after switching problem or language. In those states the label is plain `Hint`.
- After a failed Check it becomes `Hint 0/N`, where N is 1 or 2.
- Each click appends the next hint under the report in the result pane (`── Hint k/N ──`) and updates the label to `Hint k/N`.
- At `N/N` the button is disabled again.
- A new Check replaces the hints with the ones for the new failure. If the error changed, so do the hints.
- The hints are never saved to disk or to `progress.json`.

### What makes a hint "dynamic"

The hints are built in two layers. Both are computed from the actual failure.

**Hint 1: the diagnosis.** It says what is wrong and where, using the learner's own values. It is generated from the failure itself, with no per-problem text needed. It never says how to fix the problem.

**Hint 2: the nudge.** It points toward the idea that fixes this kind of failure on this problem. It comes from the problem's `hints.json`, chosen by the failed test or by the kind of error. It never contains solution code.

### Failure details, which replace the plain report

`check_lang` returns `(ok, report, failure)`. `report` is built exactly as today, plus a new `RUNTIME ERROR` outcome. `failure` is `None` on a pass. Otherwise it is a dict:

```python
{"kind": "compile" | "runtime" | "timeout" | "wrong" | "missing",
 "lang": "py", "test": "3", "input": "...", "expected": "...", "got": "...",
 "stderr": "...", "returncode": -11}
```

`RUNTIME ERROR on test N` means the return code is not 0. The report still shows the input, and stderr instead of the output.

### Diagnosis rules (hint 1)

They live in `trainer.diagnose(failure)` and are checked in this order. The first rule that matches wins.

| Kind | Detected from | Hint 1 says (filled with real values) |
| --- | --- | --- |
| runtime (Python) | the last traceback line, `ExceptionType: msg`, and its `line N` | "`IndexError` on line 7 on test 4 (input shown). An index went past the end of a list." One sentence for each common exception: `ValueError` from `int()`, `ZeroDivisionError`, `RecursionError`, `IndexError`, `KeyError`. |
| runtime (C/C++) | return code −11 / −6 / −8 (SIGSEGV / SIGABRT / SIGFPE) | "Segfault on test 4: an out-of-range array index or a bad pointer." With SIGFPE: "division by zero". |
| runtime (Rust) | `panicked at … :LINE` plus the message | "Panic on line 9: `index out of bounds`." The same applies to `attempt to add with overflow` and `called unwrap() on Err`. |
| timeout | the test name, and whether it is a `.gen.py` (large) test | "Too slow on test 5, the large one (n ≈ 10⁵). The small tests pass, so the logic is right but the method is too slow." |
| wrong: empty output | `got` is empty | "Nothing was printed on test 2." For Rust or C it adds: "check that the output is printed and not only computed." |
| wrong: format only | the same tokens, with different spaces or line breaks | "The values are right. Only the format differs: expected 1 line, you printed 5." |
| wrong: extra or missing lines | a different number of lines, with the common lines equal | "Extra line 3: `debug: 4`. Leftover debug print?" or "Missing the last 2 lines." |
| wrong: sign only | the numbers differ only in sign | "Value 4 has the wrong sign (−3 vs 3). Negative inputs are handled differently." |
| wrong: off by one | the numbers differ by ±1 | "Value 2 is off by one (got 9, expected 10). Check the loop bounds and `<` vs `<=`." |
| wrong: overflow | expected > 2³¹−1, the language is not py, and got is negative or wrapped | "The expected value 5000000000 doesn't fit in a 32-bit `int`." |
| wrong: order | the same multiset of lines or tokens | "Right values, wrong order." |
| wrong: other | anything else | The first differing line: "Line 2: expected `7`, got `12`", plus the test input. |

### Per-problem nudges (hint 2): `problems/weekN/pXX_name/hints.json`

```json
{
  "tests": {
    "1": "Python's // rounds toward −∞; C rounds toward 0. Compute the quotient's magnitude, then apply the sign.",
    "3": "With a negative divisor, the remainder takes the sign of a (C rule), not of b.",
    "4": "Both operands negative: check that your truncation gives 2, not 3."
  },
  "timeout": "Sorting first lets you replace the inner loop with two pointers moving inward.",
  "runtime": "Read all numbers with one split(); the input may span several lines.",
  "wrong": "Fall back here when the failed test has no entry of its own."
}
```

The nudge is chosen by:
1. `tests[failed test]`, for a wrong answer or a runtime error on that test.
2. Otherwise `timeout`, `runtime` or `wrong`, matching the kind of failure.
3. Compile errors get no hints at all: no diagnosis and no nudge. The compiler output in the report is all the learner gets.

Writing these is the bulk of the work: about one sentence per test, for 84 problems. The tests were written for specific edge cases, so most sentences follow directly from what each test checks. A file may leave entries out, and the problem then gets only hint 1 for that failure.

### How many hints: 1 or 2

```
N = 0   for a compile error (the button stays disabled)
N = 1   for a missing file, or a format-only / empty-output diagnosis
        (hint 1 already points at the fix)
N = 1   for level-1 problems, unless the failure is a timeout or a runtime error
N = 2   otherwise, when hints.json has a nudge for this failure
N = 1   whenever there is no nudge available
```

The difficulty comes from the problem's `level` (from `week.json`). An optional `"hints": 1 | 2` in `hints.json` overrides it for a problem that is harder or easier than its week.

### Shared logic in `trainer.py`

```python
def check_lang(p, lang):           # -> (ok, report, failure); adds RUNTIME ERROR via returncode
def diagnose(failure):             # -> hint 1 string (rules table above)
def nudge(p, failure):             # -> hint 2 string from hints.json, or None
def hints(p, failure):             # -> [] for compile errors, else [hint1] or [hint1, hint2]
```

About 150 lines in total. Everything uses the standard library only (`re`, `json`), and all of it runs locally.

## Per-interface implementation

**GTK (`gui.py`)**
- `self.hint_btn = Gtk.Button(label="Hint")` goes after `solution_btn` in `actions`, and the old `self.hint` label is renamed `self.solution_note`.
- `check_done` stores `self.hints = trainer.hints(p, failure)` and `self.shown = 0`, and enables the button if there are hints.
- `on_hint` appends the `── Hint k/N ──` block to the result buffer.
- `select_problem` and `select_lang` clear `self.hints`.

**tkinter (`gui_tk.py`)**
- The same, with `self.button(actions, "Hint", self.on_hint)` packed after `solution_btn`.
- The disabled state uses the existing `c["disabled"]` colour.

**Web (`static/index.html` + `app.py`)**
- `/api/check` returns `{"ok", "report", "hints": [...]}`. `hints` is empty on a pass.
- `<button id="hint-btn">` goes after `#solution`, and `#hint` is renamed `#solution-note`.
- The hints stay in a JS variable and are only appended to `#result` on click, so they are only shown when asked for.

**CLI (`trainer.py`)**
- `check` prints `  (hints available: trainer.py hint P01 py)` after a failure. It does not print the hints themselves.
- `trainer.py hint P01 py [k]` re-runs the check for that language and prints hint k (default 1). After a compile error it prints only `No hints for compile errors.`

## Steps (one commit each, pushed after each)

1. ✅ **`trainer.py`:** structured `failure`, the `RUNTIME ERROR` outcome, `diagnose`, `nudge`, `hints`, and the CLI `hint` command. All existing callers are updated for the 3-tuple (`gui.py`, `gui_tk.py`, `app.py`, `selftest.py`).
2. ✅ **`hints.json` for weeks 1–2:** one sentence per test, plus `timeout`/`runtime` where they apply.
3. ✅ **`hints.json` for weeks 3–4.**
4. ✅ **GTK:** the Hint button, the reveal on click, and the reset on problem or language change. The `hint` label is renamed `solution_note`.
5. ✅ **tkinter:** the same.
6. ✅ **Web:** `hints` in the `/api/check` response, and the button.
7. ✅ **Docs:** a README section, and this plan marked done.

## Testing

**`trainer.py`** (added to `selftest.py`, running in its temporary copy):
- Deliberately broken solutions trigger each diagnosis rule, and the expected wording comes back:
  - P01 in Python with `//`: test 1, and a sign or off-by-one diagnosis
  - a missing `;` in C: a compile error, which returns no hints
  - `int(input())` on two numbers: a `ValueError`
  - a C out-of-bounds write: a segfault
  - an O(n²) three-sum: a timeout
  - a leftover debug print: an extra line
  - 32-bit `int` on a big sum: overflow
- **The hints depend on the error:** two different wrong P01 solutions that fail on different tests get different hint 1 and hint 2.
- The count rule: level 1 + wrong gives 1 hint, level 3 + wrong gives 2, a compile error gives 0, and a problem with no `hints.json` gives 1.
- Every `hints.json` parses, and its keys name tests that exist.
- No hint contains a line of `solution.py`, so a hint never leaks the solution.

**Each UI**, using the existing harnesses (GTK offscreen, tkinter on Xvfb, web in Chrome):
- The button is disabled before Check and after a pass.
- After a failure it shows `Hint 0/N`, and **nothing is shown until it is clicked**.
- Clicking reveals the hints one at a time, and at N/N the button is disabled.
- Fixing one bug and checking again changes the hints.
- Switching language or problem clears the hints.
- Light and dark screenshots.

## Size and risk

- About 150 lines in `trainer.py` and about 30 per UI, plus 84 small `hints.json` files. No new dependencies, and nothing leaves the machine.
- **`check_lang` now returns 3 values.** Every caller is updated in step 1, and `selftest.py` catches any that are missed.
- **The new `RUNTIME ERROR` outcome** changes the report text for crashing solutions, which were shown as `WRONG` before. Passing solutions are unaffected.

## Open decisions

1. **Local rules (this plan) or an LLM (e.g. Claude) to write the hints.** An LLM would read the learner's code and give freer feedback. It would also need an API key and network access, it costs money per hint, and it breaks the "fully local" goal from `PLAN.md`. Recommended: **local rules**. An LLM could be added later as an optional third hint.
2. **Whether to count hint use in `trainer.py status`** (e.g. "3 problems solved without hints"). It is left out for now to keep the feature minimal.

## Results (2026-11-24)

- **`trainer.py`:** `selftest.py` gets 15 broken solutions, and each one gives the expected hint 1:
  - P01 floor division (test 1), a negative divisor (test 3), a wrong sign, a debug print, layout only, and empty output
  - `ValueError`, a C null-pointer write (segfault), an infinite loop (small-test timeout) and an O(n³) three-sum (large-test timeout)
  - wrong order (P03), off by one (P09), and 32-bit overflow in C (P09)
  - a Python syntax error and a missing `;` in C, which get no hints

  It also checks:
  - 6 hint-count cases
  - that two different P01 errors get different hints
  - that all 84 `hints.json` files use known keys and name tests that exist
  - that no hint contains a line of `solution.py`. This caught a real leak in P15's timeout nudge, which was then reworded.
- **GTK** (offscreen): 11 checks pass.
  - The button is disabled before a check, shows `Hint 0/2` after a failure, and shows nothing until clicked. It reveals the hints one at a time and is then disabled.
  - A different error gives a different hint.
  - Switching language or problem clears the hints, and compile errors, Python syntax errors and passes give none.
  - Screenshots in light and dark. The result pane scrolls to each new hint.
- **tkinter** (Xvfb): the same 11 checks pass. They include that the hints and the revealed text survive the window rebuild on a theme change.
- **Web** (Chrome): 9 checks pass, with no console errors. `/api/check` returns `hints`, which is empty for compile errors.
- **Not tested here:** Rust panics, because `rustc` has no default toolchain on this machine (`rustup default stable` was never run), and the Windows crash codes.
- **Change from the plan:** Python syntax errors are now checked with `compile()` before the tests run and reported as `COMPILE ERROR`, so they get no hints, the same as C, C++ and Rust compile errors.
