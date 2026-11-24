#!/usr/bin/env python3
"""Local web app for the coding trainer. Run: python3 app.py, open http://localhost:8000"""
import datetime
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

import trainer

INDEX = (trainer.ROOT / "static" / "index.html").read_bytes()
LEVELS = [f"Level {n} · {week['title']}" for n, (_d, week) in enumerate(trainer.weeks(), 1)]


def problems_state(progress):
    today = datetime.date.today()
    days = []
    for p in trainer.course_problems(progress):
        if p["unlock"] > today:
            continue
        if not days or (days[-1]["week"], days[-1]["day"]) != (p["week"], p["day"]):
            days.append({"week": p["week"], "day": p["day"], "level": p["level"],
                         "date": str(p["unlock"]), "title": p["day_title"],
                         "today": p["unlock"] == today, "problems": []})
        days[-1]["problems"].append({"id": p["id"], "name": p["name"][4:],
                                     "passed": list(progress["passed"].get(p["id"], {}))})
    return {"start": progress["start"], "level": progress.get("level", 1), "days": days}


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
