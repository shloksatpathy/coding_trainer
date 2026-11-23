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
from tkinter import messagebox

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
LEVELS = [f"Level {n} · {week['title']}" for n, (_d, week) in enumerate(trainer.weeks(), 1)]


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

        self.current = None      # problem dict from trainer.course_problems
        self.code = {}           # lang -> editor text for the current problem
        self.lang = "c"
        self.result_state = ("", False)
        self.results = queue.Queue()
        self.frame = None
        self.sidebar_view = None
        self.theme_var = tk.StringVar()
        self.level_var = tk.IntVar()
        self.sidebar_var = tk.BooleanVar()
        self.build_menu()
        root.bind_all("<Control-b>", self.on_ctrl_b)
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

    def on_theme(self):
        trainer.set_setting("theme", self.theme_var.get())
        self.render()

    def watch_system_theme(self):
        if self.theme_choice() == "system" and system_dark() != self.dark:
            self.render()
        self.root.after(2000, self.watch_system_theme)

    # ---------- menu bar ----------

    def build_menu(self):
        self.menubar = tk.Menu(self.root)
        self.course_menu = tk.Menu(self.menubar, tearoff=False)
        self.level_menu = tk.Menu(self.course_menu, tearoff=False)
        for n, label in enumerate(LEVELS, 1):
            self.level_menu.add_radiobutton(label=label, variable=self.level_var, value=n, command=self.on_level)
        self.course_menu.add_cascade(label="Start at level", menu=self.level_menu)
        self.course_menu.add_separator()
        self.course_menu.add_command(label="Reset…", command=self.on_reset)
        self.view_menu = tk.Menu(self.menubar, tearoff=False)
        self.view_menu.add_checkbutton(label="Problem list", variable=self.sidebar_var, accelerator="Ctrl+B",
                                       command=self.on_sidebar)
        self.theme_menu = tk.Menu(self.view_menu, tearoff=False)
        for label, key in THEMES.items():
            self.theme_menu.add_radiobutton(label=label, variable=self.theme_var, value=key, command=self.on_theme)
        self.view_menu.add_cascade(label="Theme", menu=self.theme_menu)
        self.help_menu = tk.Menu(self.menubar, tearoff=False)
        self.help_menu.add_command(label="About Coding Trainer", command=self.on_about)
        self.menubar.add_cascade(label="Course", menu=self.course_menu)
        self.menubar.add_cascade(label="View", menu=self.view_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.root.configure(menu=self.menubar)

    def sync_menu(self):
        """Set menu marks, states and colours from progress.json (Windows draws its menu bar natively)."""
        progress = trainer.load_progress()
        settings = progress or {}
        started = trainer.is_started(progress)
        self.theme_var.set(settings.get("theme", "system"))
        self.level_var.set(settings.get("level", 1) if started else 0)
        self.sidebar_var.set(self.sidebar_open())
        state = "normal" if started else "disabled"
        self.course_menu.entryconfigure("Start at level", state=state)
        self.view_menu.entryconfigure("Problem list", state=state)
        c = self.c
        for m in (self.menubar, self.course_menu, self.level_menu, self.view_menu, self.theme_menu, self.help_menu):
            m.configure(bg=c["panel"], fg=c["text"], activebackground=c["active"], activeforeground=c["text"],
                        selectcolor=c["text"], relief="flat", bd=0)

    def sidebar_open(self):
        return (trainer.load_progress() or {}).get("sidebar", "open") == "open"

    def on_sidebar(self):
        trainer.set_setting("sidebar", "open" if self.sidebar_var.get() else "collapsed")
        self.show_sidebar(self.sidebar_var.get())

    def show_sidebar(self, visible):
        """Place or remove only the sidebar, so the editor keeps its cursor and undo history."""
        if visible:
            self.show_btn.pack_forget()
            self.side.pack(side="left", fill="y", before=self.paned)
            self.side_border.pack(side="left", fill="y", before=self.paned)
        else:
            self.side.pack_forget()
            self.side_border.pack_forget()
            self.show_btn.pack(anchor="w", padx=6, pady=(8, 0), before=self.statement)

    def toggle_sidebar(self):
        if trainer.is_started(trainer.load_progress()):
            self.sidebar_var.set(not self.sidebar_var.get())
            self.on_sidebar()

    def on_ctrl_b(self, _event):
        self.toggle_sidebar()
        return "break"  # in text widgets Ctrl+B would also move the cursor back

    def confirm(self, icon, title, message):
        return messagebox.askokcancel(title, message, icon=icon, default="cancel", parent=self.root)

    def on_level(self):
        level = self.level_var.get()
        if self.confirm("question", f"Start at level {level}?",
                        f"Level {level} starts today. Levels below {level} will be locked.\n\n"
                        "Your passed checks and saved code are kept."):
            trainer.start_course(level)
            self.current = None
        self.render()

    def on_reset(self):
        if self.confirm("warning", "Reset Coding Trainer?",
                        "This permanently deletes:\n"
                        "  • your progress (start date, level, passed checks)\n"
                        "  • ALL your saved code in work/\n"
                        "  • your settings (theme, problem list) and the test cache\n\n"
                        "It cannot be undone. Press OK to delete everything."):
            trainer.reset_course()
            self.current = None
            self.code = {}
            self.render()

    def on_about(self):
        messagebox.showinfo("About Coding Trainer", f"Coding Trainer {trainer.VERSION}\n\n"
                            "Daily coding problems in C, C++, Python and Rust.\n\n"
                            "https://github.com/shloksatpathy/coding_trainer", parent=self.root)

    # ---------- layout ----------

    def render(self):
        """(Re)build the window in the current theme, keeping the open problem and editor text."""
        if self.current:
            self.code[self.lang] = self.editor_text()
            if self.side.winfo_ismapped():
                self.sidebar_view = self.canvas.yview()[0]
        self.dark = self.is_dark()
        self.c = PALETTES["dark" if self.dark else "light"]
        if self.frame:
            self.frame.destroy()
        self.root.configure(bg=self.c["bg"])
        self.frame = tk.Frame(self.root, bg=self.c["bg"])
        self.frame.pack(fill="both", expand=True)
        if not trainer.is_started(trainer.load_progress()):
            self.build_welcome()
        else:
            self.build_main()
        self.sync_menu()

    def build_welcome(self):
        c = self.c
        box = tk.Frame(self.frame, bg=c["bg"])
        box.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(box, text="Coding Trainer", font=(self.f_h1[0], 20, "bold"), bg=c["bg"], fg=c["text"]).pack()
        tk.Label(box, text="Weekly problem sets in C, C++, Python and Rust. A new day unlocks every day.",
                 font=self.f_body, bg=c["bg"], fg=c["text"]).pack(pady=8)
        pick = tk.Frame(box, bg=c["bg"])
        pick.pack(pady=(0, 10))
        tk.Label(pick, text="Start at level", font=self.f_body, bg=c["bg"], fg=c["text"]).pack(side="left", padx=(0, 8))
        self.level_pick = tk.StringVar(value=LEVELS[0])
        menu = tk.OptionMenu(pick, self.level_pick, *LEVELS)
        menu.config(font=self.f_body, bg=c["panel"], fg=c["text"], activebackground=c["hover"],
                    activeforeground=c["text"], relief="flat", bd=0, highlightthickness=1,
                    highlightbackground=c["input_border"], padx=8)
        menu["menu"].config(font=self.f_body, bg=c["panel"], fg=c["text"], activebackground=c["active"],
                            activeforeground=c["text"])
        menu.pack(side="left")
        self.button(box, "Start today", self.on_start).pack()

    def button(self, parent, text, command):
        c = self.c
        return tk.Button(parent, text=text, command=command, font=self.f_body, bg=c["accent"], fg="#ffffff",
                         activebackground=c["accent"], activeforeground="#ffffff", disabledforeground="#ffffff",
                         relief="flat", bd=0, padx=16, pady=4, highlightthickness=0, cursor="hand2")

    def build_main(self):
        c = self.c
        # Sidebar; show_sidebar() places it when the problem list is open
        side = self.side = tk.Frame(self.frame, bg=c["panel"], width=280)
        side.pack_propagate(False)
        self.side_border = tk.Frame(self.frame, bg=c["border"], width=1)
        head = tk.Frame(side, bg=c["panel"])
        head.pack(fill="x", padx=(6, 12), pady=(12, 6))
        self.icon_button(head, c["panel"]).pack(side="left", padx=(0, 4))
        tk.Label(head, text="Coding Trainer", font=self.f_title, bg=c["panel"], fg=c["text"]).pack(side="left")

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

        # Statement, with a show-list button above it while the list is collapsed
        column = tk.Frame(paned, bg=c["bg"])
        self.show_btn = self.icon_button(column, c["bg"])
        self.statement = tk.Text(column, wrap="word", bg=c["bg"], fg=c["text"], font=self.f_body, relief="flat",
                                 bd=0, padx=24, pady=20, highlightthickness=0, cursor="arrow",
                                 selectbackground=c["active"], selectforeground=c["text"], spacing3=2)
        self.statement.tag_configure("h1", font=self.f_h1, spacing3=8)
        self.statement.tag_configure("bold", font=self.f_bold)
        self.statement.tag_configure("code", font=self.f_mono, background=c["code_bg"])
        self.statement.tag_configure("block", font=self.f_mono, background=c["code_bg"], lmargin1=10, lmargin2=10,
                                     rmargin=10, lmargincolor=c["code_bg"], rmargincolor=c["code_bg"])
        self.statement.pack(fill="both", expand=True)
        paned.add(column, width=500, minsize=300)
        self.paned = paned

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
        for text in (self.editor, self.statement, self.result):
            text.bind("<Control-b>", self.on_ctrl_b)
        self.show_sidebar(self.sidebar_open())

        self.fill_sidebar()

    def icon_button(self, parent, bg):
        c = self.c
        return tk.Button(parent, text="☰", font=(self.f_body[0], 13), command=self.toggle_sidebar, bg=bg, fg=c["text"],
                         activebackground=c["hover"], activeforeground=c["text"], relief="flat", bd=0, padx=6,
                         highlightthickness=0, cursor="hand2")

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
        today = datetime.date.today()
        self.problems = [p for p in trainer.course_problems(progress) if p["unlock"] <= today]
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
        trainer.start_course(LEVELS.index(self.level_pick.get()) + 1)
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
