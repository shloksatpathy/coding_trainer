#!/usr/bin/env python3
"""Coding trainer: a problem set every 3 days, the previous set's solutions with it, submission checker."""
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

ROOT = Path(__file__).parent
PROBLEMS = ROOT / "problems"
WORK = ROOT / "work"
PROGRESS = ROOT / "progress.json"
CACHE = ROOT / "cache"
LANGS = ["c", "cpp", "py", "rs"]
WINDOWS = os.name == "nt"
# Child Python must be python.exe: when the window app is started with pythonw.exe, sys.executable is pythonw.
PYTHON = str(Path(sys.executable).with_name("python.exe")) if WINDOWS else sys.executable
EXE = "p.exe" if WINDOWS else "p"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
LOCKED = datetime.date.max  # unlock date of levels below the chosen start level
SET_DAYS = 3  # a new problem set every 3 days; it also releases the previous set's solutions

STUBS = {
    "c": '#include <stdio.h>\n\nint main(void) {\n    // read from stdin, print to stdout\n    return 0;\n}\n',
    "cpp": '#include <iostream>\n\nint main() {\n    // read from std::cin, print to std::cout\n    return 0;\n}\n',
    "py": '# read from input(), print with print()\n',
    "rs": 'use std::io::Read;\n\nfn main() {\n    let mut input = String::new();\n    std::io::stdin().read_to_string(&mut input).unwrap();\n    // parse input, print with println!\n}\n',
}


def load_progress():
    if not PROGRESS.exists():
        return None
    return json.loads(PROGRESS.read_text(encoding="utf-8"))


def save_progress(progress):
    PROGRESS.write_text(json.dumps(progress, indent=2), encoding="utf-8")


def is_started(progress):
    """progress.json can hold only settings (theme, sidebar) before the course starts."""
    return progress is not None and "start" in progress


def set_setting(key, value):
    progress = load_progress() or {}
    progress[key] = value
    save_progress(progress)


def start_course(level, start=None):
    """Level `level` starts on `start` (default today); lower levels stay locked. Keeps passed checks and settings."""
    progress = load_progress() or {}
    progress["start"] = (start or datetime.date.today()).isoformat()
    progress["level"] = level
    progress.setdefault("passed", {})
    save_progress(progress)
    return progress


def reset_course():
    """Whole reset: progress, settings, all saved code and the test cache."""
    PROGRESS.unlink(missing_ok=True)
    for folder in (WORK, CACHE):
        if folder.exists():
            shutil.rmtree(folder)


def weeks():
    """List of (week_dir, week_data), ordered by week number."""
    dirs = sorted(PROBLEMS.glob("week*"), key=lambda d: int(d.name[4:]))
    return [(d, json.loads((d / "week.json").read_text(encoding="utf-8"))) for d in dirs]


def all_problems(start, level=1):
    """Yield dicts describing every problem with its unlock date.

    Sets of week `level` and later are released one every SET_DAYS days from `start`; a set's
    solutions unlock with the next set. Weeks below `level` are locked.
    """
    n = 0  # sets released before this one
    for w, (wdir, week) in enumerate(weeks()):
        locked = w + 1 < level
        for s, pset in enumerate(week["sets"]):
            unlock = start + datetime.timedelta(days=SET_DAYS * n)
            for name in pset["problems"]:
                yield {
                    "id": name.split("_")[0],
                    "name": name,
                    "dir": wdir / name,
                    "week": w + 1,
                    "level": week["level"],
                    "set": s + 1,
                    "set_title": pset["title"],
                    "unlock": LOCKED if locked else unlock,
                    "solution_unlock": LOCKED if locked else unlock + datetime.timedelta(days=SET_DAYS),
                    "work": WORK / wdir.name / f"day{s + 1:02d}" / name,  # folder name kept from daily sets
                }
            if not locked:
                n += 1


def course_problems(progress):
    """all_problems for a started course; files from v0.1.0 have no level and count as level 1."""
    return all_problems(datetime.date.fromisoformat(progress["start"]), progress.get("level", 1))


def lock_message(p):
    if p["unlock"] == LOCKED:
        return f"{p['id'].upper()} is locked: level {p['level']} is below your starting level"
    return f"{p['id'].upper()} unlocks on {p['unlock']}"


def find_problem(progress, pid):
    for p in course_problems(progress):
        if p["id"] == pid.lower():
            return p
    sys.exit(f"No problem {pid}")


def require_unlocked(p):
    if datetime.date.today() < p["unlock"]:
        sys.exit(lock_message(p))


def parse_level(text):
    levels = len(weeks())
    if not text.isdigit() or not 1 <= int(text) <= levels:
        sys.exit(f"Level must be 1-{levels}")
    return int(text)


def cmd_start(args):
    if is_started(load_progress()):
        sys.exit("Already started. Use `trainer.py level N` to change level or `trainer.py reset` to start over.")
    level = 1
    if "--level" in args:
        i = args.index("--level")
        level = parse_level(args[i + 1])
        args = args[:i] + args[i + 2:]
    start = datetime.date.fromisoformat(args[0]) if args else None
    progress = start_course(level, start)
    print(f"Started level {level} on {progress['start']}. Run `trainer.py list` to see the current problem set.")


def cmd_level(progress, args):
    level = parse_level(args[0])
    start_course(level)
    print(f"Level {level} starts today. Levels below {level} are locked; passed checks and saved code are kept.")


def cmd_reset(args):
    print("This permanently deletes:\n"
          "  - your progress (start date, level, passed checks)\n"
          "  - ALL your saved code in work/\n"
          "  - your settings (theme, problem list) and the test cache")
    if input('Type "reset" to confirm: ') != "reset":
        sys.exit("Nothing was deleted.")
    reset_course()
    print("Reset done. Run `trainer.py start` to begin again.")


def cmd_list(progress, args):
    today = datetime.date.today()
    current = None
    for p in course_problems(progress):
        if p["unlock"] > today:
            continue
        if (p["week"], p["set"]) != current:
            current = (p["week"], p["set"])
            mark = "  <- current" if today < p["solution_unlock"] else ""
            print(f"\nWeek {p['week']} (level {p['level']}) · Set {p['set']} · {p['unlock']} · {p['set_title']}{mark}")
        done = progress["passed"].get(p["id"], {})
        langs = " ".join(f"{l}:{'✅' if l in done else '☐'}" for l in LANGS)
        print(f"  {p['id'].upper()}  {p['name'][4:]:<22} {langs}")


def cmd_show(progress, args):
    p = find_problem(progress, args[0])
    require_unlocked(p)
    print((p["dir"] / "problem.md").read_text(encoding="utf-8"))


def cmd_init(progress, args):
    p = find_problem(progress, args[0])
    require_unlocked(p)
    p["work"].mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        f = p["work"] / f"main.{lang}"
        if not f.exists():
            f.write_text(STUBS[lang], encoding="utf-8")
    sample = p["dir"] / "tests" / "1.in"
    (p["work"] / "in.txt").write_text(sample.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Workspace ready: {p['work'].relative_to(ROOT)}")


def run_cmd(cmd, stdin=None, **kwargs):
    """Run a command with UTF-8 text I/O; on Windows without flashing a console window."""
    return subprocess.run(cmd, input=stdin, capture_output=True, encoding="utf-8", errors="replace",
                          creationflags=subprocess.CREATE_NO_WINDOW if WINDOWS else 0, **kwargs)


def run(lang, src, build, stdin):
    if lang == "py":
        cmd = [PYTHON, str(src)]
    else:
        cmd = [str(build / EXE)]
    return run_cmd(cmd, stdin, timeout=10)


def compile_src(lang, src, build):
    out = str(build / EXE)
    cmds = {
        "c": ["gcc", "-Wall", "-O2", "-o", out, str(src), "-lm"],
        "cpp": ["g++", "-std=c++17", "-Wall", "-O2", "-o", out, str(src)],
        "rs": ["rustc", "-O", "-o", out, str(src)],
    }
    if lang == "py":
        return None
    return run_cmd(cmds[lang])


def normalize(text):
    return [line.rstrip() for line in text.rstrip().splitlines()]


def test_cases(p):
    """List of (name, input, expected) for a problem.

    Small tests are stored as N.in / N.out. Large tests are N.gen.py scripts that print the
    input; the expected output comes from the reference solution. Both are cached in cache/.
    """
    tests = p["dir"] / "tests"
    names = sorted({f.name.split(".")[0] for f in tests.iterdir()}, key=int)
    cases = []
    for name in names:
        gen = tests / f"{name}.gen.py"
        if gen.exists():
            cached = CACHE / p["dir"].parent.name / p["name"]
            inp, out = cached / f"{name}.in", cached / f"{name}.out"
            if not out.exists():
                cached.mkdir(parents=True, exist_ok=True)
                inp.write_text(run_cmd([PYTHON, str(gen)], check=True).stdout, encoding="utf-8")
                out.write_text(run_cmd([PYTHON, str(p["dir"] / "solution.py")], inp.read_text(encoding="utf-8"),
                                       check=True).stdout, encoding="utf-8")
        else:
            inp, out = tests / f"{name}.in", tests / f"{name}.out"
        cases.append((name, inp.read_text(encoding="utf-8"), out.read_text(encoding="utf-8")))
    return cases


def check_lang(p, lang):
    """Return (passed, report, failure) for one language's solution; failure is None on a pass."""
    src = p["work"] / f"main.{lang}"
    if not src.exists():
        return False, f"{lang:<4} missing {src.relative_to(ROOT)}", {"kind": "missing", "lang": lang}
    if lang == "py":
        try:
            compile(src.read_text(encoding="utf-8"), str(src), "exec")
        except SyntaxError as e:
            stderr = "".join(traceback.format_exception_only(e))
            return False, f"{lang:<4} COMPILE ERROR\n{stderr}", {"kind": "compile", "lang": lang, "stderr": stderr}
    with tempfile.TemporaryDirectory() as tmp:
        build = Path(tmp)
        result = compile_src(lang, src, build)
        if result is not None and result.returncode != 0:
            return False, f"{lang:<4} COMPILE ERROR\n{result.stderr}", {"kind": "compile", "lang": lang,
                                                                       "stderr": result.stderr}
        tests = test_cases(p)
        for name, stdin, expected in tests:
            failure = {"lang": lang, "test": name, "input": stdin, "expected": expected,
                       "large": (p["dir"] / "tests" / f"{name}.gen.py").exists()}
            try:
                got = run(lang, src, build, stdin)
            except subprocess.TimeoutExpired:
                return False, f"{lang:<4} TIMEOUT on test {name}", {**failure, "kind": "timeout"}
            if got.returncode != 0:
                return False, (
                    f"{lang:<4} RUNTIME ERROR on test {name} (exit code {got.returncode})\n"
                    f"input:\n{stdin.rstrip()}\n"
                    f"{got.stderr.rstrip()}"
                ), {**failure, "kind": "runtime", "got": got.stdout, "stderr": got.stderr,
                    "returncode": got.returncode}
            if normalize(got.stdout) != normalize(expected):
                return False, (
                    f"{lang:<4} WRONG on test {name}\n"
                    f"input:\n{stdin.rstrip()}\n"
                    f"expected:\n{expected.rstrip()}\n"
                    f"got:\n{got.stdout.rstrip()}{got.stderr.rstrip()}"
                ), {**failure, "kind": "wrong", "got": got.stdout}
        return True, f"{lang:<4} PASS ({len(tests)} tests)", None


PY_ERRORS = {
    "ValueError": "A conversion such as int() got text it can't parse.",
    "ZeroDivisionError": "A division or % by zero.",
    "RecursionError": "The recursion goes too deep, or never reaches its base case.",
    "IndexError": "An index went past the end of a list or string.",
    "KeyError": "A dictionary lookup used a key that isn't in the dictionary.",
    "EOFError": "input() was called more times than there are input lines.",
}
SIGNALS = {  # return code -> what it means; POSIX signals and their Windows status codes
    -11: "Segfault: an out-of-range array index, a bad pointer, or very deep recursion.",
    3221225477: "Segfault: an out-of-range array index, a bad pointer, or very deep recursion.",
    3221225725: "Stack overflow: the recursion goes too deep, or a local array is too big.",
    -6: "Aborted: a failed assert, an uncaught C++ exception, or a .at() index out of range.",
    -8: "Integer division or % by zero.",
    3221225620: "Integer division or % by zero.",
}


def diagnose_runtime(f):
    test, err = f["test"], f["stderr"]
    if f["lang"] == "py" and err.strip():
        last = err.strip().splitlines()[-1]
        name = last.split(":")[0]
        lines = re.findall(r'File ".*main\.py", line (\d+)', err)
        where = f" on line {lines[-1]}" if lines else ""
        return f"`{last}`{where}, on test {test}. {PY_ERRORS.get(name, '')}".rstrip()
    panic = re.search(r"panicked at (?:'(.*)', )?\S*?:(\d+):\d+:?\n?(.*)", err)
    if f["lang"] == "rs" and panic:
        return f"Panic on line {panic[2]}, on test {test}: `{panic[1] or panic[3]}`."
    if f["returncode"] in SIGNALS:
        return f"Crash on test {test}. {SIGNALS[f['returncode']]}"
    return f"The program exited with code {f['returncode']} on test {test}; it should end with exit code 0."


def number(token):
    try:
        return int(token)
    except ValueError:
        return None


def is_subsequence(short, long):
    it = iter(long)
    return all(line in it for line in short)


def diagnose_wrong(f):
    test, exp, got = f["test"], normalize(f["expected"]), normalize(f["got"])
    if not f["got"].strip():
        extra = "" if f["lang"] == "py" else " Check that the result is printed, not only computed."
        return f"Nothing was printed on test {test}.{extra}"
    if " ".join(exp).split() == " ".join(got).split():
        if len(exp) != len(got):
            return f"The values are right; only the layout differs: expected {len(exp)} line(s), you printed {len(got)}."
        k = next(i for i in range(len(exp)) if exp[i] != got[i])
        return f"The values are right; only the spacing differs on line {k + 1}: expected `{exp[k]}`, got `{got[k]}`."
    if sorted(exp) == sorted(got) or sorted(" ".join(exp).split()) == sorted(" ".join(got).split()):
        return f"Right values, wrong order on test {test}."
    if len(got) > len(exp) and is_subsequence(exp, got):
        k = next(i for i in range(len(got)) if i >= len(exp) or got[i] != exp[i])
        return f"Extra line {k + 1}: `{got[k]}`. The expected lines are all there. Leftover debug print?"
    if len(got) < len(exp) and is_subsequence(got, exp):
        k = next(i for i in range(len(exp)) if i >= len(got) or got[i] != exp[i])
        return f"Missing line {k + 1}: expected `{exp[k]}`. You printed {len(got)} of {len(exp)} lines."
    if len(exp) == len(got) and all(len(e.split()) == len(g.split()) for e, g in zip(exp, got)):
        diffs = [(i, j, e, g) for i, (el, gl) in enumerate(zip(exp, got))
                 for j, (e, g) in enumerate(zip(el.split(), gl.split())) if e != g]
        where = (lambda i, j: f"value {j + 1}") if len(exp) == 1 else (lambda i, j: f"line {i + 1} value {j + 1}")
        nums = [(i, j, number(e), number(g)) for i, j, e, g in diffs]
        if all(e is not None and g is not None for _, _, e, g in nums):
            big = [e for _, _, e, g in nums if abs(e) > 2**31 - 1 and abs(g) <= 2**32]
            if big and f["lang"] != "py":
                return f"The expected value {big[0]} on test {test} doesn't fit in a 32-bit int."
            if all(e == -g for _, _, e, g in nums):
                return f"Wrong sign on test {test}: " + ", ".join(
                    f"{where(i, j)} is {g}, expected {e}" for i, j, e, g in nums[:3]) + ". The size is right."
            if all(abs(e - g) == 1 for _, _, e, g in nums):
                return f"Off by one on test {test}: " + ", ".join(
                    f"{where(i, j)} is {g}, expected {e}" for i, j, e, g in nums[:3]) + "."
        if len(diffs) <= 3:
            return f"On test {test}, " + ", ".join(
                f"{where(i, j)} is {g}, expected {e}" for i, j, e, g in diffs) + ". The other values are right."
        i, j, e, g = diffs[0]
        return f"{len(diffs)} values differ on test {test}; the first is {where(i, j)}: expected {e}, got {g}."
    k = next(i for i in range(len(exp)) if i >= len(got) or got[i] != exp[i])
    return f"First difference on test {test}, line {k + 1}: expected `{exp[k]}`, got `{got[k] if k < len(got) else ''}`."


def diagnose(f):
    """Hint 1: what is wrong and where, from the learner's own failure. Never explains compile errors."""
    if f["kind"] == "missing":
        return f"There is no main.{f['lang']} yet. Write your solution and check again."
    if f["kind"] == "runtime":
        return diagnose_runtime(f)
    if f["kind"] == "timeout":
        size = len(f["input"].split())
        if f["large"]:
            return (f"Too slow on test {f['test']}, a large one ({size} values in the input). The tests before it "
                    f"pass, so the logic is probably right but the method is too slow for this size.")
        return (f"Too slow on test {f['test']}, which is small ({size} values in the input). "
                f"That points to a loop that never ends, or reading more input than there is.")
    return diagnose_wrong(f)


def problem_hints(p):
    f = p["dir"] / "hints.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def nudge(p, f):
    """Hint 2: the idea that fixes this failure on this problem, from hints.json; None if there is none."""
    data = problem_hints(p)
    if f["kind"] in ("wrong", "runtime") and f["test"] in data.get("tests", {}):
        return data["tests"][f["test"]]
    return data.get(f["kind"])


def hints(p, f):
    """[] for a pass or a compile error, else [diagnosis] or [diagnosis, nudge]."""
    if f is None or f["kind"] == "compile":
        return []
    first, second = diagnose(f), nudge(p, f)
    simple = f["kind"] == "missing" or (f["kind"] == "wrong" and (
        not f["got"].strip() or " ".join(normalize(f["expected"])).split() == " ".join(normalize(f["got"])).split()))
    limit = problem_hints(p).get("hints", 1 if p["level"] == 1 and f["kind"] == "wrong" else 2)
    if second is None or simple or limit == 1:
        return [first]
    return [first, second]


def record_pass(progress, p, lang):
    passed = progress["passed"].setdefault(p["id"], {})
    passed.setdefault(lang, datetime.date.today().isoformat())
    save_progress(progress)


def cmd_check(progress, args):
    p = find_problem(progress, args[0])
    require_unlocked(p)
    langs = args[1:] or LANGS
    print(f"Checking {p['id'].upper()} {p['name'][4:]}")
    for lang in langs:
        ok, report, failure = check_lang(p, lang)
        print("  " + report)
        if ok:
            record_pass(progress, p, lang)
        elif hints(p, failure):
            print(f"  (hints available: trainer.py hint {p['id'].upper()} {lang})")


def cmd_hint(progress, args):
    p = find_problem(progress, args[0])
    require_unlocked(p)
    lang, k = args[1], int(args[2]) if len(args) > 2 else 1
    ok, report, failure = check_lang(p, lang)
    if ok:
        sys.exit(report)
    if failure["kind"] == "compile":
        sys.exit("No hints for compile errors.")
    found = hints(p, failure)
    if not 1 <= k <= len(found):
        sys.exit(f"This failure has {len(found)} hint(s).")
    print(f"Hint {k}/{len(found)}: {found[k - 1]}")


def cmd_solution(progress, args):
    p = find_problem(progress, args[0])
    if p["solution_unlock"] == LOCKED:
        sys.exit(lock_message(p))
    if datetime.date.today() < p["solution_unlock"]:
        sys.exit(f"Solution for {p['id'].upper()} unlocks on {p['solution_unlock']}, with the next problem set")
    print((p["dir"] / "solution.py").read_text(encoding="utf-8"))


def cmd_status(progress, args):
    today = datetime.date.today()
    problems = list(course_problems(progress))
    for w, (wdir, week) in enumerate(weeks()):
        probs = [p for p in problems if p["week"] == w + 1]
        if probs[0]["unlock"] == LOCKED:
            continue
        if probs[0]["unlock"] > today:
            break
        total = len(probs) * len(LANGS)
        done = sum(len(progress["passed"].get(p["id"], {})) for p in probs)
        on_time = sum(
            1 for p in probs for d in progress["passed"].get(p["id"], {}).values()
            if datetime.date.fromisoformat(d) < p["solution_unlock"]
        )
        print(f"Week {w + 1} · {week['title']} (level {week['level']}): {done}/{total} solutions ({100 * done // total}%), {on_time} before the solutions")
        for lang in LANGS:
            n = sum(1 for p in probs if lang in progress["passed"].get(p["id"], {}))
            print(f"  {lang:<4} {n}/{len(probs)}")


COMMANDS = {
    "level": cmd_level,
    "list": cmd_list,
    "show": cmd_show,
    "init": cmd_init,
    "check": cmd_check,
    "hint": cmd_hint,
    "solution": cmd_solution,
    "status": cmd_status,
}

USAGE = """usage: trainer.py <command>
  start [YYYY-MM-DD] [--level N]  begin the course at level N (default: today, level 1)
  level N                restart the schedule at level N today (lower levels lock)
  reset                  delete progress, settings, all saved code and the cache
  list                   released problem sets and per-language progress
  show P01               print a problem
  init P01               create work folder with main.c/.cpp/.py/.rs and in.txt
  check P01 [c cpp py rs] run your solutions against the tests
  hint P01 py [k]        hint k (default 1) for your current failure in one language
  solution P01           reference solution (released with the next problem set)
  status                 weekly completion summary"""


def main():
    if len(sys.argv) < 2:
        sys.exit(USAGE)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "start":
        return cmd_start(args)
    if cmd == "reset":
        return cmd_reset(args)
    progress = load_progress()
    if not is_started(progress):
        sys.exit("Run `trainer.py start` first.")
    if cmd not in COMMANDS:
        sys.exit(USAGE)
    COMMANDS[cmd](progress, args)


if __name__ == "__main__":
    main()
