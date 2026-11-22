#!/usr/bin/env python3
"""Coding trainer: weekly problem sets, daily unlocks, submission checker."""
import datetime
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent
PROBLEMS = ROOT / "problems"
WORK = ROOT / "work"
PROGRESS = ROOT / "progress.json"
LANGS = ["c", "cpp", "py", "rs"]

STUBS = {
    "c": '#include <stdio.h>\n\nint main(void) {\n    // read from stdin, print to stdout\n    return 0;\n}\n',
    "cpp": '#include <iostream>\n\nint main() {\n    // read from std::cin, print to std::cout\n    return 0;\n}\n',
    "py": '# read from input(), print with print()\n',
    "rs": 'use std::io::Read;\n\nfn main() {\n    let mut input = String::new();\n    std::io::stdin().read_to_string(&mut input).unwrap();\n    // parse input, print with println!\n}\n',
}


def load_progress():
    if not PROGRESS.exists():
        return None
    return json.loads(PROGRESS.read_text())


def save_progress(progress):
    PROGRESS.write_text(json.dumps(progress, indent=2))


def weeks():
    """List of (week_dir, week_data), ordered by week number."""
    dirs = sorted(PROBLEMS.glob("week*"), key=lambda d: int(d.name[4:]))
    return [(d, json.loads((d / "week.json").read_text())) for d in dirs]


def all_problems(start):
    """Yield dicts describing every problem with its unlock date."""
    for w, (wdir, week) in enumerate(weeks()):
        week_start = start + datetime.timedelta(days=7 * w)
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
                    "unlock": week_start + datetime.timedelta(days=d),
                    "solution_unlock": week_start + datetime.timedelta(days=7),
                    "work": WORK / wdir.name / f"day{d + 1:02d}" / name,
                }


def find_problem(progress, pid):
    start = datetime.date.fromisoformat(progress["start"])
    for p in all_problems(start):
        if p["id"] == pid.lower():
            return p
    sys.exit(f"No problem {pid}")


def require_unlocked(p):
    if datetime.date.today() < p["unlock"]:
        sys.exit(f"{p['id']} unlocks on {p['unlock']}")


def cmd_start(args):
    if PROGRESS.exists():
        sys.exit("Already started. Delete progress.json to restart.")
    start = args[0] if args else datetime.date.today().isoformat()
    save_progress({"start": start, "passed": {}})
    print(f"Started on {start}. Run `trainer.py list` to see today's problems.")


def cmd_list(progress, args):
    start = datetime.date.fromisoformat(progress["start"])
    today = datetime.date.today()
    current = None
    for p in all_problems(start):
        if p["unlock"] > today:
            break
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
    print((p["dir"] / "problem.md").read_text())


def cmd_init(progress, args):
    p = find_problem(progress, args[0])
    require_unlocked(p)
    p["work"].mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        f = p["work"] / f"main.{lang}"
        if not f.exists():
            f.write_text(STUBS[lang])
    sample = p["dir"] / "tests" / "1.in"
    (p["work"] / "in.txt").write_text(sample.read_text())
    print(f"Workspace ready: {p['work'].relative_to(ROOT)}")


def run(lang, src, build, stdin):
    if lang == "py":
        cmd = [sys.executable, str(src)]
    else:
        cmd = [str(build / "p")]
    return subprocess.run(cmd, input=stdin, capture_output=True, text=True, timeout=10)


def compile_src(lang, src, build):
    out = str(build / "p")
    cmds = {
        "c": ["gcc", "-Wall", "-O2", "-o", out, str(src), "-lm"],
        "cpp": ["g++", "-std=c++17", "-Wall", "-O2", "-o", out, str(src)],
        "rs": ["rustc", "-O", "-o", out, str(src)],
    }
    if lang == "py":
        return None
    return subprocess.run(cmds[lang], capture_output=True, text=True)


def normalize(text):
    return [line.rstrip() for line in text.rstrip().splitlines()]


def check_lang(p, lang):
    src = p["work"] / f"main.{lang}"
    if not src.exists():
        print(f"  {lang:<4} missing {src.relative_to(ROOT)}")
        return False
    with tempfile.TemporaryDirectory() as tmp:
        build = Path(tmp)
        result = compile_src(lang, src, build)
        if result is not None and result.returncode != 0:
            print(f"  {lang:<4} COMPILE ERROR\n{result.stderr}")
            return False
        tests = sorted((p["dir"] / "tests").glob("*.in"), key=lambda f: int(f.stem))
        for t in tests:
            stdin = t.read_text()
            expected = t.with_suffix(".out").read_text()
            try:
                got = run(lang, src, build, stdin)
            except subprocess.TimeoutExpired:
                print(f"  {lang:<4} TIMEOUT on test {t.stem}")
                return False
            if normalize(got.stdout) != normalize(expected):
                print(f"  {lang:<4} WRONG on test {t.stem}")
                print(f"       input:\n{stdin.rstrip()}")
                print(f"       expected:\n{expected.rstrip()}")
                print(f"       got:\n{got.stdout.rstrip()}{got.stderr.rstrip()}")
                return False
        print(f"  {lang:<4} PASS ({len(tests)} tests)")
        return True


def cmd_check(progress, args):
    p = find_problem(progress, args[0])
    require_unlocked(p)
    langs = args[1:] or LANGS
    print(f"Checking {p['id'].upper()} {p['name'][4:]}")
    for lang in langs:
        if check_lang(p, lang):
            passed = progress["passed"].setdefault(p["id"], {})
            passed.setdefault(lang, datetime.date.today().isoformat())
    save_progress(progress)


def cmd_solution(progress, args):
    p = find_problem(progress, args[0])
    if datetime.date.today() < p["solution_unlock"]:
        sys.exit(f"Solution for {p['id'].upper()} unlocks on {p['solution_unlock']} (end of week {p['week']})")
    print((p["dir"] / "solution.py").read_text())


def cmd_status(progress, args):
    start = datetime.date.fromisoformat(progress["start"])
    today = datetime.date.today()
    for w, (wdir, week) in enumerate(weeks()):
        probs = [p for p in all_problems(start) if p["week"] == w + 1]
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
    "list": cmd_list,
    "show": cmd_show,
    "init": cmd_init,
    "check": cmd_check,
    "solution": cmd_solution,
    "status": cmd_status,
}

USAGE = """usage: trainer.py <command>
  start [YYYY-MM-DD]     begin the course (default: today)
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
    progress = load_progress()
    if progress is None:
        sys.exit("Run `trainer.py start` first.")
    if cmd not in COMMANDS:
        sys.exit(USAGE)
    COMMANDS[cmd](progress, args)


if __name__ == "__main__":
    main()
