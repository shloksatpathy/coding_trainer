#!/usr/bin/env python3
"""Self-test: every generator is deterministic and every reference solution passes its own tests.

Runs in a temporary copy of the project, so your work/, progress.json and cache/ are never touched.
"""
import datetime
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent

with tempfile.TemporaryDirectory() as tmp:
    copy = Path(tmp)
    shutil.copy(ROOT / "trainer.py", copy)
    shutil.copytree(ROOT / "problems", copy / "problems")
    sys.path.insert(0, str(copy))
    import trainer

    failed = 0
    gens = sorted(copy.glob("problems/*/*/tests/*.gen.py"))
    for gen in gens:
        runs = [subprocess.run([sys.executable, str(gen)], capture_output=True, text=True, check=True).stdout
                for _ in range(2)]
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

    print(f"\n{len(problems)} problems, {failed} failure(s)")
    sys.exit(1 if failed else 0)
