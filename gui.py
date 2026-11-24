#!/usr/bin/python3
"""Native window for the coding trainer (GTK 3). Run: /usr/bin/python3 gui.py"""
import datetime
import re
import threading

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import Gdk, GdkPixbuf, Gio, GLib, Gtk, Pango  # noqa: E402

import trainer  # noqa: E402

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

CSS = """
window, .main {{ background-color: {bg}; color: {text}; }}
.sidebar, .sidebar list, .sidebar row {{ background-color: {panel}; color: {text}; }}
.sidebar {{ border-right: 1px solid {border}; }}
.app-title {{ font-weight: bold; font-size: 12pt; }}
.day-header {{ color: {muted}; font-size: 8pt; font-weight: 600; }}
.day-header.today {{ color: {accent}; }}
.day-title {{ color: {muted}; font-size: 8pt; }}
.sidebar row.prob {{ border-radius: 4px; }}
.sidebar row.prob:hover {{ background-color: {hover}; }}
.sidebar row.prob:selected {{ background-color: {active}; color: {text}; }}
.dot {{ color: {dot}; font-size: 7pt; }}
.dot.ok {{ color: {ok}; }}
.statement {{ background-color: {bg}; color: {text}; }}
.codeblock {{ background-color: {code_bg}; border-radius: 4px; padding: 8px 10px; font-family: monospace; }}
.editor-pane {{ border-left: 1px solid {border}; }}
button.lang-tab {{ background-image: none; background-color: {panel}; color: {text};
                   border: 1px solid {input_border}; border-radius: 4px; padding: 2px 12px; box-shadow: none; }}
button.lang-tab label {{ color: {text}; }}
button.lang-tab.active {{ background-color: {tab_bg}; border-color: {tab_bg}; }}
button.lang-tab.active label {{ color: {tab_fg}; }}
textview.editor {{ font-family: monospace; font-size: 10pt; }}
textview.editor text {{ background-color: {panel}; color: {text}; }}
.editor-frame {{ border: 1px solid {input_border}; border-radius: 4px; }}
button.primary {{ background-image: none; background-color: {accent}; border: none; border-radius: 4px;
                  padding: 4px 16px; box-shadow: none; }}
button.primary label {{ color: #ffffff; }}
button.primary:disabled {{ background-color: {disabled}; }}
.note {{ color: {muted}; }}
textview.result {{ font-family: monospace; font-size: 9pt; }}
textview.result text {{ background-color: {result_bg}; color: #eeeeee; }}
textview.result.ok text {{ color: #7ee787; }}
.result-frame {{ background-color: {result_bg}; border-radius: 4px; }}
menubar {{ background-color: {panel}; border-bottom: 1px solid {border}; padding: 0; }}
menubar > menuitem {{ color: {text}; padding: 4px 10px; }}
menubar > menuitem:hover {{ background-color: {hover}; }}
menubar > menuitem label {{ color: {text}; }}
button.icon {{ background-image: none; background-color: transparent; border: none; box-shadow: none;
               color: {text}; padding: 0 6px; min-height: 0; min-width: 0; }}
button.icon label {{ color: {text}; font-size: 13pt; }}
button.icon:hover {{ background-color: {hover}; }}
combobox button {{ background-image: none; background-color: {panel}; color: {text};
                   border: 1px solid {input_border}; box-shadow: none; padding: 0 4px; min-height: 0; }}
scrollbar, scrollbar trough {{ background-color: transparent; border: none; }}
scrollbar slider {{ background-color: {input_border}; }}
paned > separator {{ background-color: {border}; background-image: none; min-width: 1px; margin: 0;
                     padding: 0; border: none; }}
.sidebar row {{ margin: 0 8px; }}
"""


def markdown_widgets(md, palette):
    """Turn the problem markdown into labels and code blocks, like the web page does."""
    widgets = []
    parts = re.split(r"```[a-z]*\n(.*?)```", md, flags=re.S)
    for i, part in enumerate(parts):
        if i % 2:
            label = Gtk.Label(label=part.rstrip("\n"), xalign=0, selectable=True)
            label.get_style_context().add_class("codeblock")
            widgets.append(label)
            continue
        for block in re.split(r"\n\n+", part.strip()):
            if not block:
                continue
            text = GLib.markup_escape_text(block)
            text = re.sub(r"`([^`]+)`", rf'<span font_family="monospace" background="{palette["code_bg"]}"> \1 </span>', text)
            text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
            if text.startswith("# "):
                text = f'<span size="x-large" weight="bold">{text[2:]}</span>'
            label = Gtk.Label(xalign=0, selectable=True, wrap=True)
            label.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
            label.set_markup(text)
            widgets.append(label)
    return widgets


class TrainerWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Coding Trainer")
        self.set_default_size(1400, 800)
        self.connect("destroy", Gtk.main_quit)

        self.css = Gtk.CssProvider()
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.css,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        self.desktop = Gio.Settings.new("org.gnome.desktop.interface")
        self.desktop.connect("changed::color-scheme", lambda *a: self.apply_theme())

        self.current = None      # problem dict from trainer.course_problems
        self.code = {}           # lang -> editor text for the current problem
        self.lang = "c"
        self.rows = {}           # problem id -> (row, [dot labels])
        self.syncing = False     # True while menus are set from progress.json, so their handlers stay quiet
        self.accel = Gtk.AccelGroup()
        self.add_accel_group(self.accel)

        outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(outer)
        outer.add(self.build_menu())
        self.stack = Gtk.Stack(vexpand=True)
        outer.add(self.stack)
        self.stack.add_named(self.build_welcome(), "welcome")
        self.stack.add_named(self.build_main(), "main")
        self.apply_theme()
        self.show_all()
        self.show_screen()

    def show_screen(self):
        """Welcome screen before the course starts, the problem view after."""
        progress = trainer.load_progress()
        self.sync_menus(progress)
        if trainer.is_started(progress):
            self.load()
        else:
            self.level_pick.set_active_id("1")
            self.stack.set_visible_child_name("welcome")

    # ---------- menu bar ----------

    def build_menu(self):
        bar = Gtk.MenuBar()

        def menu(label):
            item = Gtk.MenuItem(label=label, use_underline=True)
            sub = Gtk.Menu()
            item.set_submenu(sub)
            bar.append(item)
            return sub

        def radio_group(parent, entries, handler):
            items, group = {}, None
            for key, label in entries:
                item = Gtk.RadioMenuItem.new_with_label_from_widget(group, label)
                group = item
                item.connect("toggled", handler, key)
                parent.append(item)
                items[key] = item
            return items

        course = menu("_Course")
        self.level_item = Gtk.MenuItem(label="Start at level")
        levels = Gtk.Menu()
        self.level_item.set_submenu(levels)
        self.level_items = radio_group(levels, [(n, f"Level {n} · {week['title']}")
                                                for n, (_d, week) in enumerate(trainer.weeks(), 1)], self.on_level_item)
        course.append(self.level_item)
        course.append(Gtk.SeparatorMenuItem())
        reset = Gtk.MenuItem(label="Reset…")
        reset.connect("activate", self.on_reset)
        course.append(reset)

        view = menu("_View")
        self.sidebar_item = Gtk.CheckMenuItem(label="Problem list")
        self.sidebar_item.add_accelerator("activate", self.accel, Gdk.KEY_b, Gdk.ModifierType.CONTROL_MASK,
                                          Gtk.AccelFlags.VISIBLE)
        self.sidebar_item.connect("toggled", self.on_sidebar_item)
        view.append(self.sidebar_item)
        theme = Gtk.MenuItem(label="Theme")
        themes = Gtk.Menu()
        theme.set_submenu(themes)
        self.theme_items = radio_group(themes, [("system", "System"), ("light", "Light"), ("dark", "Dark")],
                                       self.on_theme_item)
        view.append(theme)

        help_menu = menu("_Help")
        about = Gtk.MenuItem(label="About Coding Trainer")
        about.connect("activate", self.on_about)
        help_menu.append(about)
        return bar

    def sync_menus(self, progress):
        """Set menu marks and the sidebar from progress.json without triggering their handlers."""
        settings = progress or {}
        started = trainer.is_started(progress)
        sidebar_open = settings.get("sidebar", "open") == "open"
        self.syncing = True
        self.theme_items[settings.get("theme", "system")].set_active(True)
        if started:
            self.level_items[settings.get("level", 1)].set_active(True)
        self.sidebar_item.set_active(sidebar_open)
        self.syncing = False
        self.level_item.set_sensitive(started)
        self.sidebar_item.set_sensitive(started)
        self.show_sidebar(sidebar_open)

    def on_level_item(self, item, level):
        if self.syncing or not item.get_active():
            return
        if self.confirm(self.level_dialog(level)):
            trainer.start_course(level)
            self.show_screen()
        else:
            self.sync_menus(trainer.load_progress())

    def on_theme_item(self, item, key):
        if self.syncing or not item.get_active():
            return
        trainer.set_setting("theme", key)
        self.apply_theme()

    def on_sidebar_item(self, item):
        if self.syncing:
            return
        trainer.set_setting("sidebar", "open" if item.get_active() else "collapsed")
        self.show_sidebar(item.get_active())

    def toggle_sidebar(self, *_):
        self.sidebar_item.set_active(not self.sidebar_item.get_active())

    def show_sidebar(self, visible):
        self.revealer.set_reveal_child(visible)
        self.show_list_btn.set_visible(not visible)

    # ---------- dialogs ----------

    def dialog(self, kind, title, text, ok_label, destructive=False):
        d = Gtk.MessageDialog(transient_for=self, modal=True, message_type=kind, buttons=Gtk.ButtonsType.NONE,
                              text=title)
        d.format_secondary_text(text)
        d.add_button("Cancel", Gtk.ResponseType.CANCEL)
        ok = d.add_button(ok_label, Gtk.ResponseType.OK)
        if destructive:
            ok.get_style_context().add_class("destructive-action")
        d.set_default_response(Gtk.ResponseType.CANCEL)
        return d

    def confirm(self, d):
        answer = d.run()
        d.destroy()
        return answer == Gtk.ResponseType.OK

    def level_dialog(self, level):
        return self.dialog(Gtk.MessageType.QUESTION, f"Start at level {level}?",
                           f"Level {level} starts today. Levels below {level} will be locked.\n"
                           "Your passed checks and saved code are kept.", f"Start level {level}")

    def reset_dialog(self):
        return self.dialog(Gtk.MessageType.WARNING, "Reset Coding Trainer?",
                           "This permanently deletes:\n"
                           "  • your progress (start date, level, passed checks)\n"
                           "  • ALL your saved code in work/\n"
                           "  • your settings (theme, problem list) and the test cache\n\n"
                           "It cannot be undone.", "Delete everything", destructive=True)

    def on_reset(self, _item):
        if self.confirm(self.reset_dialog()):
            trainer.reset_course()
            self.current = None
            self.apply_theme()
            self.show_screen()

    def on_about(self, _item):
        logo = GdkPixbuf.Pixbuf.new_from_file_at_size(str(trainer.ROOT / "desktop" / "coding-trainer.svg"), 96, 96)
        d = Gtk.AboutDialog(transient_for=self, modal=True, program_name="Coding Trainer", version=trainer.VERSION,
                            comments="Daily coding problems in C, C++, Python and Rust",
                            website="https://github.com/shloksatpathy/coding_trainer", logo=logo)
        d.run()
        d.destroy()

    # ---------- layout ----------

    def build_welcome(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, valign=Gtk.Align.CENTER,
                      halign=Gtk.Align.CENTER)
        box.get_style_context().add_class("main")
        title = Gtk.Label()
        title.set_markup('<span size="xx-large" weight="bold">Coding Trainer</span>')
        box.add(title)
        box.add(Gtk.Label(label="Weekly problem sets in C, C++, Python and Rust. A new day unlocks every day."))
        pick = Gtk.Box(spacing=8, halign=Gtk.Align.CENTER)
        pick.add(Gtk.Label(label="Start at level"))
        self.level_pick = Gtk.ComboBoxText()
        for n, (_d, week) in enumerate(trainer.weeks(), 1):
            self.level_pick.append(str(n), f"Level {n} · {week['title']}")
        pick.add(self.level_pick)
        box.add(pick)
        start = Gtk.Button(label="Start today", halign=Gtk.Align.CENTER)
        start.get_style_context().add_class("primary")
        start.connect("clicked", self.on_start)
        box.add(start)
        return box

    def build_main(self):
        root = Gtk.Box()
        root.get_style_context().add_class("main")

        # Sidebar
        side = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        side.set_size_request(280, -1)
        side.set_hexpand(False)
        side.get_style_context().add_class("sidebar")
        head = Gtk.Box(margin=12, margin_start=6, margin_bottom=6, spacing=4)
        head.add(self.icon_button("☰", "Hide problem list (Ctrl+B)"))
        title = Gtk.Label(label="Coding Trainer", xalign=0, hexpand=True)
        title.get_style_context().add_class("app-title")
        head.add(title)
        side.add(head)
        self.side_scroll = Gtk.ScrolledWindow(vexpand=True, hscrollbar_policy=Gtk.PolicyType.NEVER)
        self.listbox = Gtk.ListBox()
        self.listbox.connect("row-activated", lambda lb, row: self.open_problem(row.pid))
        self.side_scroll.add(self.listbox)
        side.add(self.side_scroll)
        self.revealer = Gtk.Revealer(transition_type=Gtk.RevealerTransitionType.SLIDE_RIGHT, transition_duration=150)
        self.revealer.add(side)
        root.add(self.revealer)

        paned = Gtk.Paned(hexpand=True)
        paned.set_position(500)

        # Statement
        scroll = Gtk.ScrolledWindow(hscrollbar_policy=Gtk.PolicyType.NEVER)
        scroll.get_style_context().add_class("statement")
        self.statement = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin=24, margin_top=20)
        scroll.add(self.statement)
        column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        column.get_style_context().add_class("statement")
        self.show_list_btn = self.icon_button("☰", "Show problem list (Ctrl+B)")
        self.show_list_btn.set_halign(Gtk.Align.START)
        self.show_list_btn.set_margin_start(6)
        self.show_list_btn.set_margin_top(8)
        self.show_list_btn.set_no_show_all(True)
        column.add(self.show_list_btn)
        scroll.set_vexpand(True)
        column.add(scroll)
        paned.pack1(column, resize=True, shrink=False)

        # Editor pane
        editor = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8, margin=12)
        wrap = Gtk.Box()
        wrap.get_style_context().add_class("editor-pane")
        wrap.pack_start(editor, True, True, 0)

        tabs = Gtk.Box(spacing=4)
        self.tab_buttons = {}
        for lang in trainer.LANGS:
            b = Gtk.Button(label=NAMES[lang])
            b.get_style_context().add_class("lang-tab")
            b.connect("clicked", lambda _b, l=lang: self.select_lang(l))
            self.tab_buttons[lang] = b
            tabs.add(b)
        editor.add(tabs)

        frame = Gtk.ScrolledWindow(vexpand=True)
        frame.get_style_context().add_class("editor-frame")
        self.editor = Gtk.TextView(monospace=True, left_margin=10, right_margin=10, top_margin=10,
                                   bottom_margin=10)
        self.editor.get_style_context().add_class("editor")
        self.editor.connect("key-press-event", self.on_editor_key)
        frame.add(self.editor)
        editor.add(frame)

        actions = Gtk.Box(spacing=8)
        self.check_btn = Gtk.Button(label="Check")
        self.check_btn.get_style_context().add_class("primary")
        self.check_btn.connect("clicked", self.on_check)
        self.solution_btn = Gtk.Button(label="Reference solution")
        self.solution_btn.get_style_context().add_class("primary")
        self.solution_btn.connect("clicked", self.on_solution)
        self.hint_btn = Gtk.Button(label="Hint")
        self.hint_btn.get_style_context().add_class("primary")
        self.hint_btn.connect("clicked", self.on_hint)
        self.solution_note = Gtk.Label()
        self.solution_note.get_style_context().add_class("note")
        actions.add(self.check_btn)
        actions.add(self.solution_btn)
        actions.add(self.hint_btn)
        actions.add(self.solution_note)
        self.set_hints([])
        editor.add(actions)

        out = Gtk.ScrolledWindow()
        out.set_size_request(-1, 220)
        out.get_style_context().add_class("result-frame")
        self.result = Gtk.TextView(editable=False, cursor_visible=False, monospace=True, wrap_mode=Gtk.WrapMode.WORD_CHAR,
                                   left_margin=10, right_margin=10, top_margin=10, bottom_margin=10)
        self.result.get_style_context().add_class("result")
        out.add(self.result)
        editor.add(out)

        paned.pack2(wrap, resize=True, shrink=False)
        root.add(paned)
        return root

    def icon_button(self, text, tooltip):
        b = Gtk.Button(label=text, tooltip_text=tooltip)
        b.get_style_context().add_class("icon")
        b.connect("clicked", self.toggle_sidebar)
        return b

    # ---------- theme ----------

    def theme_choice(self):
        progress = trainer.load_progress()
        return progress.get("theme", "system") if progress else "system"

    def apply_theme(self):
        choice = self.theme_choice()
        dark = choice == "dark" or (choice == "system" and self.desktop.get_string("color-scheme") == "prefer-dark")
        self.palette = PALETTES["dark" if dark else "light"]
        Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", dark)
        self.css.load_from_data(CSS.format(**self.palette).encode())
        if self.current:
            self.render_statement()

    # ---------- data ----------

    def on_start(self, _button):
        trainer.start_course(int(self.level_pick.get_active_id()))
        self.show_screen()

    def load(self):
        progress = trainer.load_progress()
        for child in self.listbox.get_children():
            self.listbox.remove(child)
        self.rows = {}
        self.current = None
        today = datetime.date.today()
        self.problems = [p for p in trainer.course_problems(progress) if p["unlock"] <= today]
        last_day = None
        today_header = None
        for p in self.problems:
            if (p["week"], p["day"]) != last_day:
                last_day = (p["week"], p["day"])
                is_today = p["unlock"] == today
                header = Gtk.ListBoxRow(selectable=False, activatable=False)
                box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, margin_top=10)
                label = Gtk.Label(xalign=0, label=f"W{p['week']} · L{p['level']} · DAY {p['day']} · {p['unlock']}"
                                  + (" · TODAY" if is_today else ""))
                label.get_style_context().add_class("day-header")
                if is_today:
                    label.get_style_context().add_class("today")
                    today_header = header
                title = Gtk.Label(xalign=0, label=p["day_title"])
                title.get_style_context().add_class("day-title")
                box.add(label)
                box.add(title)
                header.add(box)
                self.listbox.add(header)
            row = Gtk.ListBoxRow()
            row.pid = p["id"]
            row.get_style_context().add_class("prob")
            box = Gtk.Box(margin=4, margin_start=6, margin_end=6)
            box.pack_start(Gtk.Label(label=f"{p['id'].upper()} {p['name'][4:].replace('_', ' ')}", xalign=0,
                                     ellipsize=Pango.EllipsizeMode.END), True, True, 0)
            dots = []
            for lang in trainer.LANGS:
                dot = Gtk.Label(label="●", tooltip_text=NAMES[lang])
                dot.get_style_context().add_class("dot")
                box.pack_start(dot, False, False, 1)
                dots.append(dot)
            row.add(box)
            self.listbox.add(row)
            self.rows[p["id"]] = (row, dots)
        self.update_dots(progress)
        self.listbox.show_all()
        self.stack.set_visible_child_name("main")
        last = self.problems[-1]
        self.open_problem(next(p["id"] for p in self.problems if (p["week"], p["day"]) == (last["week"], last["day"])))
        GLib.idle_add(self.scroll_to, today_header or self.rows[last["id"]][0])

    def scroll_to(self, row):
        alloc = row.get_allocation()
        self.side_scroll.get_vadjustment().set_value(alloc.y)

    def update_dots(self, progress):
        for pid, (_row, dots) in self.rows.items():
            passed = progress["passed"].get(pid, {})
            for lang, dot in zip(trainer.LANGS, dots):
                ctx = dot.get_style_context()
                if lang in passed:
                    ctx.add_class("ok")
                else:
                    ctx.remove_class("ok")

    # ---------- problem view ----------

    def open_problem(self, pid):
        self.current = next(p for p in self.problems if p["id"] == pid)
        self.listbox.select_row(self.rows[pid][0])
        self.code = {}
        for lang in trainer.LANGS:
            f = self.current["work"] / f"main.{lang}"
            self.code[lang] = f.read_text() if f.exists() else trainer.STUBS[lang]
        self.render_statement()
        self.set_result("", False)
        unlocked = datetime.date.today() >= self.current["solution_unlock"]
        self.solution_btn.set_sensitive(unlocked)
        self.solution_note.set_text("" if unlocked else f"Solution unlocks {self.current['solution_unlock']}")
        self.set_hints([])
        self.editor.get_buffer().set_text(self.code[self.lang])
        self.mark_tab()

    def render_statement(self):
        for child in self.statement.get_children():
            self.statement.remove(child)
        md = (self.current["dir"] / "problem.md").read_text()
        for w in markdown_widgets(md, self.palette):
            self.statement.add(w)
        self.statement.show_all()

    def editor_text(self):
        buf = self.editor.get_buffer()
        return buf.get_text(buf.get_start_iter(), buf.get_end_iter(), True)

    def select_lang(self, lang):
        self.code[self.lang] = self.editor_text()
        self.lang = lang
        self.editor.get_buffer().set_text(self.code[lang])
        self.mark_tab()
        self.set_hints([])

    def mark_tab(self):
        for lang, b in self.tab_buttons.items():
            ctx = b.get_style_context()
            if lang == self.lang:
                ctx.add_class("active")
            else:
                ctx.remove_class("active")

    def on_editor_key(self, _view, event):
        if event.keyval == Gdk.KEY_Tab:
            self.editor.get_buffer().insert_at_cursor("    ")
            return True
        return False

    def set_result(self, text, ok):
        self.result.get_buffer().set_text(text)
        ctx = self.result.get_style_context()
        if ok:
            ctx.add_class("ok")
        else:
            ctx.remove_class("ok")

    # ---------- actions ----------

    def on_check(self, _button):
        p, lang = self.current, self.lang
        self.code[lang] = self.editor_text()
        p["work"].mkdir(parents=True, exist_ok=True)
        (p["work"] / f"main.{lang}").write_text(self.code[lang])
        (p["work"] / "in.txt").write_text((p["dir"] / "tests" / "1.in").read_text())
        self.check_btn.set_sensitive(False)
        self.set_result(f"Checking {NAMES[lang]}...", False)
        self.set_hints([])

        def work():
            ok, report, failure = trainer.check_lang(p, lang)
            GLib.idle_add(self.check_done, p, lang, ok, report, failure)

        threading.Thread(target=work, daemon=True).start()

    def check_done(self, p, lang, ok, report, failure):
        progress = trainer.load_progress()
        if ok:
            trainer.record_pass(progress, p, lang)
        self.update_dots(progress)
        if self.current is p and self.lang == lang:
            self.set_result(report, ok)
            self.set_hints(trainer.hints(p, failure))
        self.check_btn.set_sensitive(True)

    def on_solution(self, _button):
        solution = (self.current["dir"] / "solution.py").read_text()
        self.set_result("# Reference solution (Python)\n\n" + solution, False)
        self.set_hints([])

    def set_hints(self, hints, shown=0):
        """Hints for the last failed check; they are only shown one at a time on click."""
        self.hints, self.shown = hints, shown
        self.hint_btn.set_label(f"Hint {shown}/{len(hints)}" if hints else "Hint")
        self.hint_btn.set_sensitive(shown < len(hints))

    def on_hint(self, _button):
        buf = self.result.get_buffer()
        k = self.shown + 1
        buf.insert(buf.get_end_iter(), f"\n\n── Hint {k}/{len(self.hints)} ──\n{self.hints[k - 1]}")
        buf.place_cursor(buf.get_end_iter())
        self.result.scroll_to_mark(buf.get_insert(), 0, False, 0, 0)
        self.set_hints(self.hints, k)


if __name__ == "__main__":
    # Matches StartupWMClass in the launcher written by install-desktop.sh, so the dock groups the window.
    Gdk.set_program_class("coding-trainer")
    GLib.set_application_name("Coding Trainer")
    Gtk.Window.set_default_icon_from_file(str(trainer.ROOT / "desktop" / "coding-trainer.svg"))
    TrainerWindow()
    Gtk.main()
