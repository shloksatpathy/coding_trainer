#!/usr/bin/env python3
"""Self-test: every generator is deterministic and every reference solution passes its own tests.

Runs in a temporary copy of the project, so your work/, progress.json and cache/ are never touched.
"""
import datetime
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent

with tempfile.TemporaryDirectory() as tmp:
    copy = Path(tmp)
    shutil.copy(ROOT / "trainer.py", copy)
    shutil.copy(ROOT / "VERSION", copy)
    shutil.copytree(ROOT / "problems", copy / "problems")
    sys.path.insert(0, str(copy))
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
        ok, report = trainer.check_lang(p, "py")
        print(f"{p['id'].upper()} {report}")
        if not ok:
            failed += 1

    # Start level: week N starts on the start date, later weeks every 7 days, lower weeks locked.
    day0 = datetime.date(2030, 1, 7)
    week = datetime.timedelta(days=7)
    levels = len(trainer.weeks())
    for level in range(1, levels + 1):
        for p in trainer.all_problems(day0, level):
            if p["week"] < level:
                ok = p["unlock"] == p["solution_unlock"] == trainer.LOCKED
            else:
                week_start = day0 + (p["week"] - level) * week
                ok = (p["unlock"] == week_start + datetime.timedelta(days=p["day"] - 1)
                      and p["solution_unlock"] == week_start + week)
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
        "reset keeps the program": (copy / "trainer.py").exists() and (copy / "problems").exists(),
    }
    for name, ok in checks.items():
        if not ok:
            print(f"FAILED: {name}")
            failed += 1
    print(f"{len(checks)} start/reset checks")

    print(f"\n{len(problems)} problems, {failed} failure(s)")
    sys.exit(1 if failed else 0)
