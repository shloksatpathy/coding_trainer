#!/usr/bin/env python3
"""Self-test: every generator is deterministic and every reference solution passes its own tests.

Runs in a temporary copy of the project, so your work/, progress.json and cache/ are never touched.
"""
import datetime
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent.parent

with tempfile.TemporaryDirectory() as tmp:
    copy = Path(tmp)
    (copy / "src").mkdir()
    shutil.copy(ROOT / "src" / "trainer.py", copy / "src")
    shutil.copy(ROOT / "VERSION", copy)
    shutil.copytree(ROOT / "problems", copy / "problems")
    sys.path.insert(0, str(copy / "src"))
    import trainer

    failed = 0
    gens = sorted(copy.glob("problems/*/*/tests/*.gen.py"))
    for gen in gens:
        runs = [trainer.run_cmd([trainer.PYTHON, str(gen)], check=True).stdout for _ in range(2)]
        if runs[0] != runs[1]:
            print(f"NOT DETERMINISTIC {gen.relative_to(copy)}")
            failed += 1
    print(f"{len(gens)} generators checked")

    problems = list(trainer.all_problems(datetime.date(2000, 1, 1)))
    for p in problems:
        p["work"].mkdir(parents=True)
        shutil.copy(p["dir"] / "solution.py", p["work"] / "main.py")
        ok, report, _failure = trainer.check_lang(p, "py")
        print(f"{p['id'].upper()} {report}")
        if not ok:
            failed += 1

    # Start level: week N's first set on the start date, then a set every 3 days; a set's solutions
    # unlock with the next set; lower weeks locked. Every week has 7 sets.
    day0 = datetime.date(2030, 1, 7)
    levels = len(trainer.weeks())
    for level in range(1, levels + 1):
        for p in trainer.all_problems(day0, level):
            if p["week"] < level:
                ok = p["unlock"] == p["solution_unlock"] == trainer.LOCKED
            else:
                n = 7 * (p["week"] - level) + p["set"] - 1
                ok = (p["unlock"] == day0 + datetime.timedelta(days=3 * n)
                      and p["solution_unlock"] == day0 + datetime.timedelta(days=3 * (n + 1)))
            if not ok:
                print(f"LEVEL {level} WRONG SCHEDULE {p['id']}: {p['unlock']} / {p['solution_unlock']}")
                failed += 1
    print(f"level schedules checked for levels 1-{levels}")

    # A v0.1.0 progress file has no "level": same schedule as level 1 from the same start.
    old = [p["unlock"] for p in trainer.course_problems({"start": day0.isoformat(), "passed": {}})]
    if old != [p["unlock"] for p in trainer.all_problems(day0, 1)]:
        print("V0.1.0 PROGRESS FILE GIVES A DIFFERENT SCHEDULE")
        failed += 1

    # Settings before starting, start keeps them, reset removes progress, settings, code and cache.
    trainer.reset_course()
    trainer.set_setting("theme", "dark")
    before = trainer.load_progress()
    progress = trainer.start_course(3, day0)
    (trainer.WORK / "x").mkdir(parents=True)
    (trainer.CACHE / "y").mkdir(parents=True)
    trainer.reset_course()
    checks = {
        "settings only before start": before == {"theme": "dark"} and not trainer.is_started(before),
        "start keeps settings": progress == {"theme": "dark", "start": day0.isoformat(), "level": 3, "passed": {}},
        "reset removes progress, work, cache": not any(x.exists() for x in (trainer.PROGRESS, trainer.WORK, trainer.CACHE)),
        "reset keeps the program": (copy / "src" / "trainer.py").exists() and (copy / "problems").exists(),
    }
    for name, ok in checks.items():
        if not ok:
            print(f"FAILED: {name}")
            failed += 1
    print(f"{len(checks)} start/reset checks")

    # Every hints.json: known keys, tests that exist, and no line of the reference solution.
    for p in problems:
        data = trainer.problem_hints(p)
        names = {f.name.split(".")[0] for f in (p["dir"] / "tests").iterdir()}
        code = [line.strip() for line in (p["dir"] / "solution.py").read_text(encoding="utf-8").splitlines()]
        texts = list(data.get("tests", {}).values()) + [data[k] for k in ("timeout", "runtime", "wrong") if k in data]
        problems_found = [
            set(data) - {"tests", "timeout", "runtime", "wrong", "hints"},
            set(data.get("tests", {})) - names,
            {line for line in code if len(line) >= 12 for text in texts if line in text},
        ]
        if any(problems_found):
            print(f"BAD HINTS {p['id']}: {problems_found}")
            failed += 1
    print(f"{sum(1 for p in problems if (p['dir'] / 'hints.json').exists())} hints.json files checked")

    # Hints: each broken solution gets the diagnosis for its own error (hint 1).
    by_id = {p["id"]: p for p in problems}

    def attempt(pid, lang, code):
        p = by_id[pid]
        p["work"].mkdir(parents=True, exist_ok=True)
        (p["work"] / f"main.{lang}").write_text(code, encoding="utf-8")
        _ok, _report, failure = trainer.check_lang(p, lang)
        return p, failure, trainer.hints(p, failure)

    P01 = "a, b = map(int, input().split())\n"
    C_MAIN = "#include <stdio.h>\nint main(void) {\n%s\n    return 0;\n}\n"
    cases = [  # (name, problem, lang, code, expected kind, text that hint 1 must contain)
        ("floor division", "p01", "py", P01 + "print(a+b, a-b, a*b, a//b, a%b)\n", "wrong",
         "On test 1, value 4 is -4, expected -3, value 5 is 1, expected -1."),
        ("negative divisor", "p01", "py", P01 + "q = -(-a // b) if a < 0 else a // b\nprint(a+b, a-b, a*b, q, a-b*q)\n",
         "wrong", "On test 3, value 4 is -4, expected -3"),
        ("wrong sign", "p01", "py", P01 + "q = int(a / b)\nprint(a+b, b-a, a*b, q, a-b*q)\n", "wrong",
         "Wrong sign on test 1: value 2 is 9, expected -9."),
        ("debug print", "p01", "py", P01 + "print('debug', a)\nq = int(a / b)\nprint(a+b, a-b, a*b, q, a-b*q)\n",
         "wrong", "Extra line 1: `debug -7`."),
        ("layout", "p01", "py", P01 + "q = int(a / b)\nfor x in (a+b, a-b, a*b, q, a-b*q):\n    print(x)\n", "wrong",
         "expected 1 line(s), you printed 5"),
        ("empty output", "p01", "py", "a, b = map(int, input().split())\n", "wrong", "Nothing was printed on test 1."),
        ("one int() for two numbers", "p01", "py", "a = int(input())\n", "runtime", "ValueError"),
        ("python syntax error", "p01", "py", "print(1\n", "compile", None),
        ("missing ;", "p01", "c", C_MAIN % '    printf("1\\n")', "compile", None),
        ("wrong order", "p03", "py", "a, b = input().split()\nprint(a, b)\n", "wrong", "Right values, wrong order"),
        ("off by one", "p09", "py", "n = int(input())\nf = [0, 1]\nwhile len(f) < n:\n    f.append(f[-1] + f[-2])\n"
         "print(*f[:n])\nprint(92)\n", "wrong", "Off by one on test 1: line 2 value 1 is 92, expected 93."),
        ("32-bit overflow", "p09", "c", C_MAIN % "    int n, a = 0, b = 1;\n    scanf(\"%d\", &n);\n"
         "    for (int i = 0; i < n; i++) { printf(i ? \" %d\" : \"%d\", a); int t = a + b; a = b; b = t; }\n"
         "    printf(\"\\n93\\n\");", "wrong", "doesn't fit in a 32-bit int"),
        ("null pointer write", "p01", "c", C_MAIN % "    volatile int *q = 0;\n    *q = 1;", "runtime",
         "Segfault"),
        ("infinite loop", "p01", "py", "while True:\n    pass\n", "timeout", "which is small"),
        ("O(n^3) three sum", "p46", "py", "n = int(input())\nv = sorted(map(int, input().split()))\nout = set()\n"
         "for i in range(n):\n    for j in range(i + 1, n):\n        for k in range(j + 1, n):\n"
         "            if v[i] + v[j] + v[k] == 0:\n                out.add((v[i], v[j], v[k]))\n"
         "print('\\n'.join(' '.join(map(str, t)) for t in sorted(out)) or 'None')\n", "timeout", "a large one"),
    ]
    first_hints = {}
    for name, pid, lang, code, kind, text in cases:
        p, failure, found = attempt(pid, lang, code)
        first_hints[name] = found[0] if found else None
        ok = failure["kind"] == kind and (found == [] if text is None else text in found[0])
        if not ok:
            print(f"HINT CASE FAILED: {name}: {failure['kind']} {found}")
            failed += 1
    if first_hints["floor division"] == first_hints["negative divisor"]:
        print("HINT CASE FAILED: two different errors got the same hint")
        failed += 1

    # How many hints: a nudge in hints.json makes 2, except for level 1 wrong answers, simple diagnoses and "hints": 1.
    p01, p46 = by_id["p01"], by_id["p46"]
    (p01["dir"] / "hints.json").write_text('{"tests": {"1": "n1"}, "runtime": "nr"}', encoding="utf-8")
    (p46["dir"] / "hints.json").write_text('{"tests": {"1": "n46"}}', encoding="utf-8")
    counts = {
        "level 1 wrong": (attempt("p01", "py", P01 + "print(a+b, a-b, a*b, a//b, a%b)\n")[2], 1),
        "level 1 runtime": (attempt("p01", "py", "a = int(input())\n")[2], 2),
        "level 1 empty output": (attempt("p01", "py", P01)[2], 1),
        "level 3 wrong": (attempt("p46", "py", "print('None')\n")[2], 2),
        "level 3 no nudge for test": (attempt("p46", "py", "n = int(input())\nprint('-1 -1 2\\n-1 0 1')\n")[2], 1),
    }
    (p46["dir"] / "hints.json").write_text('{"tests": {"1": "n46"}, "hints": 1}', encoding="utf-8")
    counts["\"hints\": 1 override"] = (attempt("p46", "py", "print('None')\n")[2], 1)
    for name, (found, n) in counts.items():
        if len(found) != n:
            print(f"HINT COUNT FAILED: {name}: {found}")
            failed += 1
    print(f"{len(cases)} hint diagnoses and {len(counts)} hint counts checked")

    print(f"\n{len(problems)} problems, {failed} failure(s)")
    sys.exit(1 if failed else 0)
