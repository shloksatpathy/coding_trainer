#!/usr/bin/env python3
"""Coding trainer: weekly problem sets, daily unlocks, submission checker."""
import datetime
import json
import os
import shutil
import subprocess
import sys
import tempfile
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

    Week `level` starts on `start`; later weeks follow every 7 days. Weeks below `level` are locked.
    """
    for w, (wdir, week) in enumerate(weeks()):
        locked = w + 1 < level
        week_start = start + datetime.timedelta(days=7 * (w + 1 - level))
        for d, day in enumerate(week["days"]):
            for name in day["problems"]:
                yield {
                    "id": name.split("_")[0],
                    "name": name,
                    "dir": wdir / name,
                    "week": w + 1,
                    "level": week["level"],
                    "day": d + 1,
                    "day_title": day["title"],
                    "unlock": LOCKED if locked else week_start + datetime.timedelta(days=d),
                    "solution_unlock": LOCKED if locked else week_start + datetime.timedelta(days=7),
                    "work": WORK / wdir.name / f"day{d + 1:02d}" / name,
                }


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
    print(f"Started level {level} on {progress['start']}. Run `trainer.py list` to see today's problems.")


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
        if (p["week"], p["day"]) != current:
            current = (p["week"], p["day"])
            mark = "  <- today" if p["unlock"] == today else ""
            print(f"\nWeek {p['week']} (level {p['level']}) · Day {p['day']} · {p['unlock']} · {p['day_title']}{mark}")
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
    """Return (passed, report) for one language's solution."""
    src = p["work"] / f"main.{lang}"
    if not src.exists():
        return False, f"{lang:<4} missing {src.relative_to(ROOT)}"
    with tempfile.TemporaryDirectory() as tmp:
        build = Path(tmp)
        result = compile_src(lang, src, build)
        if result is not None and result.returncode != 0:
            return False, f"{lang:<4} COMPILE ERROR\n{result.stderr}"
        tests = test_cases(p)
        for name, stdin, expected in tests:
            try:
                got = run(lang, src, build, stdin)
            except subprocess.TimeoutExpired:
                return False, f"{lang:<4} TIMEOUT on test {name}"
            if normalize(got.stdout) != normalize(expected):
                return False, (
                    f"{lang:<4} WRONG on test {name}\n"
                    f"input:\n{stdin.rstrip()}\n"
                    f"expected:\n{expected.rstrip()}\n"
                    f"got:\n{got.stdout.rstrip()}{got.stderr.rstrip()}"
                )
        return True, f"{lang:<4} PASS ({len(tests)} tests)"


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
        ok, report = check_lang(p, lang)
        print("  " + report)
        if ok:
            record_pass(progress, p, lang)


def cmd_solution(progress, args):
    p = find_problem(progress, args[0])
    if p["solution_unlock"] == LOCKED:
        sys.exit(lock_message(p))
    if datetime.date.today() < p["solution_unlock"]:
        sys.exit(f"Solution for {p['id'].upper()} unlocks on {p['solution_unlock']} (end of week {p['week']})")
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
            if datetime.date.fromisoformat(d) == p["unlock"]
        )
        print(f"Week {w + 1} · {week['title']} (level {week['level']}): {done}/{total} solutions ({100 * done // total}%), {on_time} on the day")
        for lang in LANGS:
            n = sum(1 for p in probs if lang in progress["passed"].get(p["id"], {}))
            print(f"  {lang:<4} {n}/{len(probs)}")


COMMANDS = {
    "level": cmd_level,
    "list": cmd_list,
    "show": cmd_show,
    "init": cmd_init,
    "check": cmd_check,
    "solution": cmd_solution,
    "status": cmd_status,
}

USAGE = """usage: trainer.py <command>
  start [YYYY-MM-DD] [--level N]  begin the course at level N (default: today, level 1)
  level N                restart the schedule at level N today (lower levels lock)
  reset                  delete progress, settings, all saved code and the cache
  list                   unlocked days and per-language progress
  show P01               print a problem
  init P01               create work folder with main.c/.cpp/.py/.rs and in.txt
  check P01 [c cpp py rs] run your solutions against the tests
  solution P01           reference solution (after the week ends)
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
