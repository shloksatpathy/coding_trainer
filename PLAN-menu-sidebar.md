# PLAN: collapsible problem list, menu bar, start level, reset

## Goal

1. **Collapsible problem list.** The sidebar can be hidden, and the statement and editor then take its 280 px.
2. **Menu bar** with:
   - **Start at level…** so a learner can begin at Level 1–4 instead of always at Level 1
   - **Reset…** to start the course over
   - the theme choice, and the sidebar toggle

This applies to all three interfaces, which already share `trainer.py`:

| Interface | File | Used on |
| --- | --- | --- |
| GTK window | `gui.py` | Linux |
| tkinter window | `gui_tk.py` | Windows (also runs on Linux) |
| Web app | `app.py` + `static/index.html` | any browser |

## Where things are today (v0.1.0)

- Layout in all three: `[sidebar 280px | statement | editor]`. The sidebar holds the title, the **theme selector** and the day/problem list.
- The schedule comes from one date: `progress["start"]`. Week *w* (= level *w*) starts on `start + 7·(w−1)`. Day *d* of it unlocks on `week_start + (d−1)`, and its solutions on `week_start + 7`.
- Starting the course writes `{"start": today, "passed": {}}`. Nothing can be reset except by deleting `progress.json` by hand.
- Theme is stored in `progress.json` (`"theme"`) for the two windows, and in `localStorage` for the web app.

**Consequence:** collapsing the sidebar as it is would also hide the theme selector, so the theme moves into the menu bar.

## Design

### Layout

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Course   View   Help                                                         │  ← menu bar
├────────────────────┬────────────────────────────┬────────────────────────────┤
│ ☰  Coding Trainer  │ P64 · Breadth-first search │ [C] [C++] [Python] [Rust]  │
│ W4 · L4 · DAY 1    │ ...                        │ editor                     │
│  P64 bfs     ○○●○  │                            │                            │
│  ...               │                            │ [Check] [Reference sol.]   │
└────────────────────┴────────────────────────────┴────────────────────────────┘

Collapsed (Ctrl+B or ☰):
┌──────────────────────────────────────────────────────────────────────────────┐
│ Course   View   Help                                                         │
├─────────────────────────────────────┬────────────────────────────────────────┤
│ ☰  P64 · Breadth-first search       │ [C] [C++] [Python] [Rust]              │
│ ...                                 │ editor (wider)                         │
└─────────────────────────────────────┴────────────────────────────────────────┘
```

**Sidebar toggle**
- Toggled three ways: the **☰** button, **View ▸ Problem list** (a check item), or **Ctrl+B**.
- The ☰ button sits at the left of the sidebar header when open. When the sidebar is collapsed, it moves to the top-left of the statement pane, so there is always a visible way back.
- When collapsed, the statement/editor split keeps its ratio and both panes widen.
- The state is remembered: `"sidebar": "open" | "collapsed"` in `progress.json` for the two windows, and `localStorage.sidebar` for the web app (where the theme already lives).

**Menu bar**

| Menu | Items |
| --- | --- |
| **Course** | Start at level ▸ 1 · 2 · 3 · 4 … · Reset… |
| **View** | ☑ Problem list (Ctrl+B) · Theme ▸ ◉ System ○ Light ○ Dark |
| **Help** | About Coding Trainer (version from `VERSION`, link to the repo) |

The theme selector is removed from the sidebar header; the menu is now its only home.

### Start at level N

**Rule** (decided): starting at level *N* means **Level N, Day 1 unlocks today**.
- Levels **below N stay locked** for as long as the course runs at that level. They aren't listed, can't be opened or checked, and their solutions stay hidden.
- Levels above N unlock week by week as before.

**Implementation:** store the chosen level next to the start date. Moving the start date back would have unlocked the lower levels, so that shortcut doesn't fit this rule.

```json
{"start": "2026-11-23", "level": 3, "passed": {...}}
```

`all_problems(start, level)`:
- For week *w* ≥ N: `week_start = start + 7·(w − N)`. Days and solutions unlock from there exactly as today.
- For week *w* < N: `unlock = solution_unlock = date.max`, meaning never. Everything that already checks `p["unlock"] <= today` keeps working unchanged.
- The "unlocks on …" messages say "locked: the course started at level N" for these problems, instead of printing `9999-12-31`.

A `progress.json` from v0.1.0 has no `"level"` key and is read as level 1, so existing courses behave exactly as before.

**Where you choose it:**
- **Welcome screen:** a "Start at level" picker (1–4, default 1) next to **Start today**.
- **Course ▸ Start at level ▸ N**, mid-course. A confirmation dialog: "Level N starts today. Levels below N will be locked. Your passed checks and saved code are kept." This sets `start = today` and `level = N`.
- The menu marks the current start level with ◉.

**CLI:** `trainer.py start [YYYY-MM-DD] [--level N]`. A new `trainer.py level N` changes the level mid-course.

### Reset

**Rule** (decided): Reset is a **whole reset**. It puts the trainer back to a fresh install. **Course ▸ Reset…** opens:

```
Reset Coding Trainer?
This permanently deletes:
  • your progress (start date, level, passed checks)
  • ALL your saved code in work/
  • your settings (theme, problem list) and the test cache
It cannot be undone.
                                   [Cancel]  [Delete everything]
```

- **Delete everything:** removes `progress.json`, `work/` and `cache/`. The window returns to the welcome screen with default settings (System theme, problem list open).
- **Cancel** is the default button, so pressing Enter never resets by accident.
- **CLI:** `trainer.py reset` lists the same three items and asks `Type "reset" to confirm:`. Anything else aborts.

### Shared logic in `trainer.py` (one place, used by all four front ends)

```python
def all_problems(start, level=1):       # weeks below `level` locked (unlock = date.max)
def course_problems(progress):           # all_problems(start, level) from a progress dict (level defaults to 1)
def start_course(level, today=None):     # start = today, level = N; keeps passed and settings
def reset_course():                      # deletes progress.json, work/ and cache/
def set_setting(key, value):             # theme / sidebar in progress.json
```

Settings can be changed on the welcome screen, before any start date exists, so `progress.json` may hold only settings, e.g. `{"theme": "dark"}`. Every UI therefore shows the welcome screen when `"start"` is missing, not when the file is missing.

## Per-interface implementation

**GTK (`gui.py`)**
- Wrap `root` in a vertical box with a `Gtk.MenuBar` on top.
- Accelerators come from a `Gtk.AccelGroup`: `<Control>b` for the sidebar.
- The level and theme items are `Gtk.RadioMenuItem` groups; "Problem list" is a `Gtk.CheckMenuItem`.
- Collapse with a `Gtk.Revealer` (slide-right transition, ~150 ms) around the sidebar, so the paned pane widens smoothly.
- Dialogs are `Gtk.MessageDialog`; the Reset dialog adds a `Gtk.CheckButton` for "also delete code".
- CSS for the menu bar uses the existing palette variables, so it follows the theme.

**tkinter (`gui_tk.py`)**
- `tk.Menu` menubar via `root.config(menu=...)`; level and theme are `radiobutton` entries on an `IntVar` / `StringVar`; "Problem list" is a `checkbutton`.
- Ctrl+B through `root.bind_all("<Control-b>")`.
- Collapse: `side.pack_forget()` and the border frame; re-pack with `before=paned` to restore.
- Reset is `messagebox.askokcancel(..., icon="warning", default="cancel")`.
- On Windows the menu bar is native, and tk cannot recolour it in dark mode; it stays the system colour. Everything below it follows the theme as now.

**Web (`static/index.html` + `app.py`)**
- A slim HTML menu bar using `<details>` dropdowns (no library), styled with the existing CSS variables.
- Collapse with `body.collapsed nav { display: none }`; `main` is `flex: 1`, so it takes the space.
- New endpoints: `POST /api/start {level}`, `POST /api/level {level}`, `POST /api/reset`. Confirmations use an in-page `<dialog>`, not `alert()`/`confirm()`.
- The web app keeps its theme and sidebar state in `localStorage`. Reset clears those too, so the reset is whole in the browser as well.

## Steps (one commit each, pushed after each)

1. **`trainer.py`:** `level` in `all_problems`, `course_problems`, `start_course`, `reset_course`, `set_setting`; welcome-screen check based on `"start"`; CLI `start --level`, `level`, `reset`.
2. **GTK:** menu bar, Revealer sidebar with ☰ and Ctrl+B, level picker on the welcome screen, level and reset dialogs, theme moved to View; uses `course_problems` so lower levels are locked.
3. **tkinter:** the same features.
4. **Web:** the same features plus the three endpoints.
5. **Docs:** README sections, and this plan marked done.
6. **Release v0.2.0:** bump `VERSION`, `make dist` + `build dist`, tag, GitHub release with notes.

## Testing

**`trainer.py`** (added to `selftest.py`):
- Level math: for N = 1…4 with a fixed `today`, week N day 1 unlocks today, day 2 tomorrow, and week N+1 in 7 days. Every problem in weeks below N is locked, solutions included, on any date. Week N's solutions unlock at `today + 7`.
- A v0.1.0 `progress.json` without `"level"` produces exactly the same schedule as before.
- `reset_course` removes `progress.json`, `work/` and `cache/`, and nothing else in the folder.
- Everything runs in the temporary copy, as `selftest.py` already does. Your real `progress.json` is never touched.

**Each UI**, driven by the existing harnesses (GTK offscreen, tkinter on Xvfb, web in Chrome) for each UI:
- Collapse via ☰, the menu and Ctrl+B. The statement + editor width grows by about the sidebar width (measured from widget sizes). Expanding restores the old width and scroll position.
- The collapsed state survives a restart.
- Start at level 3 from the welcome screen shows W3 Day 1 as today, and no W1–W2 problems are listed or openable.
- Changing the level mid-course keeps the green dots of visible problems.
- Reset → Cancel changes nothing. Reset → Delete everything leaves no `progress.json`, `work/` or `cache/`, and shows the welcome screen.
- The theme from the View menu still applies and persists.
- Screenshots in light and dark, collapsed and expanded.

## Size and risk

- About 300 lines across the four front ends plus about 60 in `trainer.py`. No new dependencies, and no change to the problem data.
- **`progress.json` format:** only new optional keys (`level`, `sidebar`); a v0.1.0 file keeps working.
- **Biggest behaviour change:** the welcome screen now depends on `"start"` rather than on whether the file exists. Step 1 updates every UI's check, and the tests cover it.
- **Not testable here:** Windows-only behaviour (the native menu bar look in `gui_tk.py`). Same caveat as v0.1.0.

## Decisions (2026-11-23)

1. Starting at a higher level keeps the **lower levels locked**.
2. Reset is a **whole reset**: progress, all saved code, settings and cache are deleted.
3. The **web app** gets all of these features too.
