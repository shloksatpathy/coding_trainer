#!/usr/bin/env python3
"""Local web app for the coding trainer. Run: python3 src/app.py, open http://localhost:8000"""
import datetime
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

import trainer

INDEX = (trainer.ROOT / "src" / "static" / "index.html").read_bytes()
LEVELS = [f"Level {n} · {week['title']}" for n, (_d, week) in enumerate(trainer.weeks(), 1)]


def problems_state(progress):
    today = datetime.date.today()
    sets = []
    for p in trainer.course_problems(progress):
        if p["unlock"] > today:
            continue
        if not sets or (sets[-1]["week"], sets[-1]["set"]) != (p["week"], p["set"]):
            sets.append({"week": p["week"], "set": p["set"], "level": p["level"],
                         "date": str(p["unlock"]), "title": p["set_title"],
                         "current": today < p["solution_unlock"], "problems": []})
        sets[-1]["problems"].append({"id": p["id"], "name": p["name"][4:],
                                     "passed": list(progress["passed"].get(p["id"], {}))})
    return {"start": progress["start"], "level": progress.get("level", 1), "sets": sets}


def problem_detail(p):
    code = {}
    for lang in trainer.LANGS:
        f = p["work"] / f"main.{lang}"
        code[lang] = f.read_text(encoding="utf-8") if f.exists() else trainer.STUBS[lang]
    solution = None
    if datetime.date.today() >= p["solution_unlock"]:
        solution = (p["dir"] / "solution.py").read_text(encoding="utf-8")
    return {"id": p["id"], "statement": (p["dir"] / "problem.md").read_text(encoding="utf-8"), "code": code,
            "solution": solution, "solution_unlock": str(p["solution_unlock"])}


def capsule_state(progress):
    lang = trainer.capsule(progress)["lang"]
    questions = trainer.capsule_problems(lang)
    passed = trainer.capsule_passed(progress, lang)
    modules = []
    for p in questions:
        if not modules or modules[-1]["n"] != p["module"]:
            modules.append({"n": p["module"], "title": p["module_title"], "passed": 0, "questions": []})
        state = "passed" if p["id"] in passed else "open" if trainer.capsule_open(progress, p, lang) else "locked"
        modules[-1]["passed"] += state == "passed"
        modules[-1]["questions"].append({"id": p["id"], "title": p["title"], "state": state})
    first = next((p["id"] for p in questions if p["id"] not in passed), questions[-1]["id"])
    return {"lang": lang, "passed": len(passed), "total": len(questions), "first": first, "modules": modules}


def capsule_detail(progress, p, lang):
    f = p["work"] / f"main.{lang}"
    return {"id": p["id"], "statement": trainer.capsule_statement(p, lang),
            "code": {lang: f.read_text(encoding="utf-8") if f.exists() else trainer.STUBS[lang]},
            "attempted": trainer.capsule_attempted(progress, p, lang),
            "passed": p["id"] in trainer.capsule_passed(progress, lang), "next": p["next"]}


def locked_message(p, lang):
    return f"{p['id'].upper()} is locked: pass {p['prev'].upper()} in {lang} first"


class Handler(BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(INDEX)
            return
        if self.path.startswith("/api/capsule"):
            progress = trainer.load_progress() or {}
            parts = self.path.split("/")[3:]  # /api/capsule or /api/capsule/<lang>/<id>
            if not parts:
                return self.send_json(capsule_state(progress))
            lang, p = parts[0], trainer.capsule_find(parts[0], parts[1])
            if not trainer.capsule_open(progress, p, lang):
                return self.send_json({"error": locked_message(p, lang)}, 403)
            return self.send_json(capsule_detail(progress, p, lang))
        progress = trainer.load_progress()
        about = {"levels": LEVELS, "version": trainer.VERSION}
        if not trainer.is_started(progress):
            return self.send_json({"started": False, **about})
        if self.path == "/api/state":
            return self.send_json({"started": True, **about, **problems_state(progress)})
        if self.path.startswith("/api/problem/"):
            p = trainer.find_problem(progress, self.path.rsplit("/", 1)[1])
            if datetime.date.today() < p["unlock"]:
                return self.send_json({"error": trainer.lock_message(p)}, 403)
            return self.send_json(problem_detail(p))
        self.send_json({"error": "not found"}, 404)

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if self.path in ("/api/start", "/api/level"):
            trainer.start_course(body["level"])
            return self.send_json({"ok": True})
        if self.path == "/api/reset":
            trainer.reset_course()
            return self.send_json({"ok": True})
        if self.path == "/api/capsule/lang":
            progress = trainer.load_progress() or {}
            trainer.capsule(progress)["lang"] = body["lang"]
            trainer.save_progress(progress)
            return self.send_json({"ok": True})
        if self.path in ("/api/capsule/check", "/api/capsule/solution"):
            progress = trainer.load_progress() or {}
            lang, p = body["lang"], trainer.capsule_find(body["lang"], body["id"])
            if not trainer.capsule_open(progress, p, lang):
                return self.send_json({"error": locked_message(p, lang)}, 403)
            if self.path == "/api/capsule/solution":
                solution = trainer.capsule_solution(progress, p, lang)
                if solution is None:
                    return self.send_json({"error": "Check this question once to unlock its solution"}, 403)
                return self.send_json({"solution": solution})
            p["work"].mkdir(parents=True, exist_ok=True)
            (p["work"] / f"main.{lang}").write_text(body["code"], encoding="utf-8")
            (p["work"] / "in.txt").write_text((p["dir"] / "tests" / "1.in").read_text(encoding="utf-8"), encoding="utf-8")
            ok, report, failure = trainer.capsule_check(progress, p, lang)
            return self.send_json({"ok": ok, "report": report, "hints": trainer.hints(p, failure)})
        if self.path == "/api/check":
            progress = trainer.load_progress()
            p = trainer.find_problem(progress, body["id"])
            if datetime.date.today() < p["unlock"]:
                return self.send_json({"error": trainer.lock_message(p)}, 403)
            p["work"].mkdir(parents=True, exist_ok=True)
            (p["work"] / f"main.{body['lang']}").write_text(body["code"], encoding="utf-8")
            (p["work"] / "in.txt").write_text((p["dir"] / "tests" / "1.in").read_text(encoding="utf-8"), encoding="utf-8")
            ok, report, failure = trainer.check_lang(p, body["lang"])
            if ok:
                trainer.record_pass(progress, p, body["lang"])
            return self.send_json({"ok": ok, "report": report, "hints": trainer.hints(p, failure)})
        self.send_json({"error": "not found"}, 404)


if __name__ == "__main__":
    print("Coding trainer running at http://localhost:8000")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
