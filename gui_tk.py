#!/usr/bin/env python3
"""Desktop window for the coding trainer built with tkinter, which ships with Python on Windows.

Same layout and features as gui.py (GTK). Run: pyw gui_tk.py (Windows) or python3 gui_tk.py
"""
import datetime
import queue
import re
import subprocess
import threading
import tkinter as tk
from tkinter import font as tkfont

import trainer

NAMES = {"c": "C", "cpp": "C++", "py": "Python", "rs": "Rust"}

PALETTES = {
    "light": dict(bg="#fafafa", panel="#ffffff", text="#1d1d1f", muted="#666666", border="#dddddd",
                  input_border="#cccccc", hover="#f0f0f0", active="#e3eefb", code_bg="#f0f0f0",
                  accent="#0a66c2", disabled="#999999", dot="#dddddd", ok="#2e9e44",
                  tab_bg="#1d1d1f", tab_fg="#ffffff", result_bg="#1d1d1f"),
    "dark": dict(bg="#16181c", panel="#1e2126", text="#e6e6e6", muted="#9aa0a6", border="#33373d",
                 input_border="#444a52", hover="#2a2e34", active="#1f3550", code_bg="#2a2e34",
                 accent="#2f7de1", disabled="#555555", dot="#444a52", ok="#3fb950",
                 tab_bg="#e6e6e6", tab_fg="#16181c", result_bg="#0d0f12"),
}
THEMES = {"System": "system", "Light": "light", "Dark": "dark"}


def system_dark():
    """True when the operating system is set to a dark theme."""
    if trainer.WINDOWS:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        return winreg.QueryValueEx(key, "AppsUseLightTheme")[0] == 0
    out = subprocess.run(["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
                         capture_output=True, text=True).stdout
    return "dark" in out


class App:
    def __init__(self, root):
        self.root = root
        root.title("Coding Trainer")
        root.geometry("1400x800")
        self.icon = tk.PhotoImage(file=str(trainer.ROOT / "desktop" / "coding-trainer.png"))
        root.iconphoto(True, self.icon)

        ui = tkfont.nametofont("TkDefaultFont").actual()["family"]
        mono = tkfont.nametofont("TkFixedFont").actual()["family"]
        self.f_body, self.f_bold = (ui, 10), (ui, 10, "bold")
        self.f_small, self.f_small_bold = (ui, 8), (ui, 8, "bold")
        self.f_title, self.f_h1 = (ui, 12, "bold"), (ui, 16, "bold")
        self.f_mono, self.f_mono_small = (mono, 10), (mono, 9)

        self.current = None      # problem dict from trainer.all_problems
        self.code = {}           # lang -> editor text for the current problem
        self.lang = "c"
        self.result_state = ("", False)
        self.results = queue.Queue()
        self.frame = None
        self.sidebar_view = None
        self.render()
        root.after(2000, self.watch_system_theme)
        root.after(100, self.poll_results)

    # ---------- theme ----------

    def theme_choice(self):
        progress = trainer.load_progress()
        return progress.get("theme", "system") if progress else "system"

    def is_dark(self):
        choice = self.theme_choice()
        return choice == "dark" or (choice == "system" and system_dark())

    def on_theme(self, label):
        progress = trainer.load_progress()
        progress["theme"] = THEMES[label]
        trainer.save_progress(progress)
        self.render()

    def watch_system_theme(self):
        if self.theme_choice() == "system" and system_dark() != self.dark:
            self.render()
        self.root.after(2000, self.watch_system_theme)

    # ---------- layout ----------

    def render(self):
        """(Re)build the window in the current theme, keeping the open problem and editor text."""
        if self.current:
            self.code[self.lang] = self.editor_text()
            self.sidebar_view = self.canvas.yview()[0]
        self.dark = self.is_dark()
        self.c = PALETTES["dark" if self.dark else "light"]
        if self.frame:
            self.frame.destroy()
        self.root.configure(bg=self.c["bg"])
        self.frame = tk.Frame(self.root, bg=self.c["bg"])
        self.frame.pack(fill="both", expand=True)
        if trainer.load_progress() is None:
            self.build_welcome()
        else:
            self.build_main()

    def build_welcome(self):
        c = self.c
        box = tk.Frame(self.frame, bg=c["bg"])
        box.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(box, text="Coding Trainer", font=(self.f_h1[0], 20, "bold"), bg=c["bg"], fg=c["text"]).pack()
        tk.Label(box, text="Weekly problem sets in C, C++, Python and Rust. A new day unlocks every day.",
                 font=self.f_body, bg=c["bg"], fg=c["text"]).pack(pady=8)
        self.button(box, "Start today", self.on_start).pack()

    def button(self, parent, text, command):
        c = self.c
        return tk.Button(parent, text=text, command=command, font=self.f_body, bg=c["accent"], fg="#ffffff",
                         activebackground=c["accent"], activeforeground="#ffffff", disabledforeground="#ffffff",
                         relief="flat", bd=0, padx=16, pady=4, highlightthickness=0, cursor="hand2")

    def build_main(self):
        c = self.c
        # Sidebar
        side = tk.Frame(self.frame, bg=c["panel"], width=280)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)
        tk.Frame(self.frame, bg=c["border"], width=1).pack(side="left", fill="y")
        head = tk.Frame(side, bg=c["panel"])
        head.pack(fill="x", padx=12, pady=(12, 6))
        tk.Label(head, text="Coding Trainer", font=self.f_title, bg=c["panel"], fg=c["text"]).pack(side="left")
        choice = self.theme_choice()
        self.theme_var = tk.StringVar(value=next(k for k, v in THEMES.items() if v == choice))
        menu = tk.OptionMenu(head, self.theme_var, *THEMES, command=self.on_theme)
        menu.config(font=self.f_body, bg=c["panel"], fg=c["text"], activebackground=c["hover"],
                    activeforeground=c["text"], relief="flat", bd=0, highlightthickness=1,
                    highlightbackground=c["input_border"], indicatoron=False, padx=8)
        menu["menu"].config(font=self.f_body, bg=c["panel"], fg=c["text"], activebackground=c["active"],
                            activeforeground=c["text"])
        menu.pack(side="right")

        self.canvas = tk.Canvas(side, bg=c["panel"], highlightthickness=0, bd=0)
        self.canvas.pack(fill="both", expand=True)
        self.list = tk.Frame(self.canvas, bg=c["panel"])
        self.canvas.create_window((0, 0), window=self.list, anchor="nw", tags="list")
        self.list.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfigure("list", width=e.width))
        self.canvas.bind("<Enter>", lambda e: self.wheel(True))
        self.canvas.bind("<Leave>", lambda e: self.wheel(False))

        paned = tk.PanedWindow(self.frame, orient="horizontal", sashwidth=1, bg=c["border"], bd=0,
                               sashrelief="flat", opaqueresize=True)
        paned.pack(side="left", fill="both", expand=True)

        # Statement
        self.statement = tk.Text(paned, wrap="word", bg=c["bg"], fg=c["text"], font=self.f_body, relief="flat",
                                 bd=0, padx=24, pady=20, highlightthickness=0, cursor="arrow",
                                 selectbackground=c["active"], selectforeground=c["text"], spacing3=2)
        self.statement.tag_configure("h1", font=self.f_h1, spacing3=8)
        self.statement.tag_configure("bold", font=self.f_bold)
        self.statement.tag_configure("code", font=self.f_mono, background=c["code_bg"])
        self.statement.tag_configure("block", font=self.f_mono, background=c["code_bg"], lmargin1=10, lmargin2=10,
                                     rmargin=10, lmargincolor=c["code_bg"], rmargincolor=c["code_bg"])
        paned.add(self.statement, width=500, minsize=300)

        # Editor pane
        pane = tk.Frame(paned, bg=c["bg"])
        paned.add(pane, minsize=400)
        tabs = tk.Frame(pane, bg=c["bg"])
        tabs.pack(side="top", fill="x", padx=12, pady=(12, 8))
        self.tabs = {}
        for lang in trainer.LANGS:
            b = tk.Button(tabs, text=NAMES[lang], font=self.f_body, relief="flat", bd=0, padx=12, pady=2,
                          highlightthickness=1, highlightbackground=c["input_border"],
                          highlightcolor=c["input_border"], cursor="hand2",
                          command=lambda l=lang: self.select_lang(l))
            b.pack(side="left", padx=(0, 4))
            self.tabs[lang] = b

        self.result = tk.Text(pane, height=13, wrap="word", bg=c["result_bg"], fg="#eeeeee",
                              font=self.f_mono_small, relief="flat", bd=0, padx=10, pady=10, highlightthickness=0)
        self.result.pack(side="bottom", fill="x", padx=12, pady=(0, 12))

        actions = tk.Frame(pane, bg=c["bg"])
        actions.pack(side="bottom", fill="x", padx=12, pady=8)
        self.check_btn = self.button(actions, "Check", self.on_check)
        self.check_btn.pack(side="left")
        self.solution_btn = self.button(actions, "Reference solution", self.on_solution)
        self.solution_btn.pack(side="left", padx=8)
        self.hint = tk.Label(actions, font=self.f_body, bg=c["bg"], fg=c["muted"])
        self.hint.pack(side="left")

        border = tk.Frame(pane, bg=c["input_border"], padx=1, pady=1)
        border.pack(side="top", fill="both", expand=True, padx=12)
        self.editor = tk.Text(border, wrap="none", undo=True, bg=c["panel"], fg=c["text"], insertbackground=c["text"],
                              font=self.f_mono, relief="flat", bd=0, padx=10, pady=10, highlightthickness=0,
                              selectbackground=c["active"], selectforeground=c["text"])
        self.editor.pack(fill="both", expand=True)
        self.editor.bind("<Tab>", self.on_tab)

        self.fill_sidebar()

    def wheel(self, on):
        if on:
            self.root.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(-1 if e.delta > 0 else 1, "units"))
            self.root.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))
            self.root.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))
        else:
            for seq in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
                self.root.unbind_all(seq)

    # ---------- sidebar ----------

    def fill_sidebar(self):
        c = self.c
        progress = trainer.load_progress()
        start = datetime.date.fromisoformat(progress["start"])
        today = datetime.date.today()
        self.problems = [p for p in trainer.all_problems(start) if p["unlock"] <= today]
        self.rows = {}
        today_header = None
        last_day = None
        for p in self.problems:
            if (p["week"], p["day"]) != last_day:
                last_day = (p["week"], p["day"])
                is_today = p["unlock"] == today
                header = tk.Frame(self.list, bg=c["panel"])
                header.pack(fill="x", padx=12, pady=(12, 2))
                text = f"W{p['week']} · L{p['level']} · DAY {p['day']} · {p['unlock']}" + (" · TODAY" if is_today else "")
                tk.Label(header, text=text, font=self.f_small_bold, bg=c["panel"],
                         fg=c["accent"] if is_today else c["muted"], anchor="w").pack(fill="x")
                tk.Label(header, text=p["day_title"], font=self.f_small, bg=c["panel"], fg=c["muted"],
                         anchor="w").pack(fill="x")
                if is_today:
                    today_header = header
            row = tk.Frame(self.list, bg=c["panel"], cursor="hand2")
            row.pack(fill="x", padx=8)
            name = tk.Label(row, text=f"{p['id'].upper()} {p['name'][4:].replace('_', ' ')}", font=self.f_body,
                            bg=c["panel"], fg=c["text"], anchor="w", padx=6, pady=3)
            name.pack(side="left", fill="x", expand=True)
            dots = [tk.Label(row, text="●", font=self.f_small, bg=c["panel"], fg=c["dot"]) for _ in trainer.LANGS]
            for dot in reversed(dots):
                dot.pack(side="right", padx=(0, 2))
            for w in [row, name, *dots]:
                w.bind("<Button-1>", lambda e, pid=p["id"]: self.open_problem(pid))
                w.bind("<Enter>", lambda e, pid=p["id"]: self.hover(pid, True))
                w.bind("<Leave>", lambda e, pid=p["id"]: self.hover(pid, False))
            self.rows[p["id"]] = (row, name, dots)
        self.update_dots(progress)

        if self.current:
            self.open_problem(self.current["id"], keep_code=True)
            self.set_result(*self.result_state)
            self.root.after_idle(self.restore_sidebar)
        else:
            last = self.problems[-1]
            first_today = next(p for p in self.problems if (p["week"], p["day"]) == (last["week"], last["day"]))
            self.open_problem(first_today["id"])
            target = today_header or self.rows[last["id"]][0]
            self.root.after_idle(lambda: self.scroll_to(target))

    def restore_sidebar(self):
        self.root.update_idletasks()
        self.canvas.yview_moveto(self.sidebar_view)

    def scroll_to(self, widget):
        self.root.update_idletasks()
        self.canvas.yview_moveto(widget.winfo_y() / self.list.winfo_height())

    def row_bg(self, pid, color):
        row, name, dots = self.rows[pid]
        for w in [row, name, *dots]:
            w.configure(bg=color)

    def hover(self, pid, inside):
        if self.current and self.current["id"] == pid:
            return
        self.row_bg(pid, self.c["hover"] if inside else self.c["panel"])

    def update_dots(self, progress):
        for pid, (_row, _name, dots) in self.rows.items():
            passed = progress["passed"].get(pid, {})
            for lang, dot in zip(trainer.LANGS, dots):
                dot.configure(fg=self.c["ok"] if lang in passed else self.c["dot"])

    # ---------- problem view ----------

    def open_problem(self, pid, keep_code=False):
        if self.current and self.current["id"] in self.rows:
            self.row_bg(self.current["id"], self.c["panel"])
        self.current = next(p for p in self.problems if p["id"] == pid)
        self.row_bg(pid, self.c["active"])
        if not keep_code:
            self.code = {}
            for lang in trainer.LANGS:
                f = self.current["work"] / f"main.{lang}"
                self.code[lang] = f.read_text(encoding="utf-8") if f.exists() else trainer.STUBS[lang]
            self.set_result("", False)
        self.render_statement()
        unlocked = datetime.date.today() >= self.current["solution_unlock"]
        self.solution_btn.configure(state="normal" if unlocked else "disabled",
                                    bg=self.c["accent"] if unlocked else self.c["disabled"])
        self.hint.configure(text="" if unlocked else f"Solution unlocks {self.current['solution_unlock']}")
        self.set_editor(self.code[self.lang])
        self.mark_tabs()

    def render_statement(self):
        md = (self.current["dir"] / "problem.md").read_text(encoding="utf-8")
        st = self.statement
        st.configure(state="normal")
        st.delete("1.0", "end")
        parts = re.split(r"```[a-z]*\n(.*?)```", md, flags=re.S)
        for i, part in enumerate(parts):
            if i % 2:
                st.insert("end", part.rstrip("\n") + "\n", "block")
                st.insert("end", "\n")
                continue
            for block in re.split(r"\n\n+", part.strip()):
                if not block:
                    continue
                if block.startswith("# "):
                    st.insert("end", block[2:], "h1")
                else:
                    for piece in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", block):
                        if piece.startswith("**"):
                            st.insert("end", piece[2:-2], "bold")
                        elif piece.startswith("`"):
                            st.insert("end", f" {piece[1:-1]} ", "code")
                        else:
                            st.insert("end", piece)
                st.insert("end", "\n\n")
        st.configure(state="disabled")

    def editor_text(self):
        return self.editor.get("1.0", "end-1c")

    def set_editor(self, text):
        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", text)
        self.editor.edit_reset()

    def select_lang(self, lang):
        self.code[self.lang] = self.editor_text()
        self.lang = lang
        self.set_editor(self.code[lang])
        self.mark_tabs()

    def mark_tabs(self):
        c = self.c
        for lang, b in self.tabs.items():
            active = lang == self.lang
            b.configure(bg=c["tab_bg"] if active else c["panel"], fg=c["tab_fg"] if active else c["text"],
                        activebackground=c["tab_bg"] if active else c["hover"],
                        activeforeground=c["tab_fg"] if active else c["text"])

    def on_tab(self, _event):
        self.editor.insert("insert", "    ")
        return "break"

    def set_result(self, text, ok):
        self.result_state = (text, ok)
        self.result.configure(state="normal", fg="#7ee787" if ok else "#eeeeee")
        self.result.delete("1.0", "end")
        self.result.insert("1.0", text)
        self.result.configure(state="disabled")

    # ---------- actions ----------

    def on_start(self):
        trainer.save_progress({"start": datetime.date.today().isoformat(), "passed": {}})
        self.render()

    def on_check(self):
        p, lang = self.current, self.lang
        self.code[lang] = self.editor_text()
        p["work"].mkdir(parents=True, exist_ok=True)
        (p["work"] / f"main.{lang}").write_text(self.code[lang], encoding="utf-8")
        (p["work"] / "in.txt").write_text((p["dir"] / "tests" / "1.in").read_text(encoding="utf-8"), encoding="utf-8")
        self.check_btn.configure(state="disabled", bg=self.c["disabled"])
        self.set_result(f"Checking {NAMES[lang]}...", False)
        threading.Thread(target=lambda: self.results.put((p, lang, *trainer.check_lang(p, lang))), daemon=True).start()

    def poll_results(self):
        while not self.results.empty():
            p, lang, ok, report = self.results.get()
            progress = trainer.load_progress()
            if ok:
                trainer.record_pass(progress, p, lang)
            self.update_dots(progress)
            if self.current["id"] == p["id"] and self.lang == lang:
                self.set_result(report, ok)
            self.check_btn.configure(state="normal", bg=self.c["accent"])
        self.root.after(100, self.poll_results)

    def on_solution(self):
        solution = (self.current["dir"] / "solution.py").read_text(encoding="utf-8")
        self.set_result("# Reference solution (Python)\n\n" + solution, False)


if __name__ == "__main__":
    if trainer.WINDOWS:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # sharp text on high-DPI screens
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("coding-trainer")  # own taskbar icon
    App(tk.Tk(className="coding-trainer"))
    tk.mainloop()
