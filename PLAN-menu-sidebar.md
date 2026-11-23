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

**Rule:** starting at level *N* means **Level N, Day 1 unlocks today**. Lower levels count as already covered: they are fully open, solutions included, for review. Higher levels unlock week by week as before.

**Implementation:** no change to the unlock logic. Store a shifted start date:

```
start = today − 7·(N − 1) days
```

The existing formulas then give: week *N* starts today; weeks below *N* started earlier, so all their days and solutions are open; week *N+1* starts in 7 days.

**Where you choose it:**
- **Welcome screen:** a "Start at level" picker (1–4, default 1) next to **Start today**.
- **Course ▸ Start at level ▸ N**, mid-course. A confirmation dialog explains the effect: "Level N starts today. Levels below N open fully. Your passed checks and saved code are kept."

Progress (`passed`) and code (`work/`) are kept, because problem ids don't change.

**CLI:** `trainer.py start [YYYY-MM-DD] [--level N]`. A new `trainer.py level N` changes the level mid-course.

### Reset

**Course ▸ Reset…** opens a confirmation dialog:

```
Reset Coding Trainer?
This clears your start date and all passed checks. It cannot be undone.
☐ Also delete my saved code (work/)
                                   [Cancel]  [Reset]
```

- **Reset:** deletes `progress.json`'s course data (`start`, `passed`) but keeps preferences (`theme`, `sidebar`). The window returns to the welcome screen.
- **Also delete my saved code:** removes `work/`. Unchecked by default.
- `cache/` is not touched. It holds only generated test data and is rebuilt anyway.
- **CLI:** `trainer.py reset [--code]` asks `Type "reset" to confirm:` before doing anything.

### Shared logic in `trainer.py` (one place, used by all four front ends)

```python
def start_course(level, today=None):      # writes start = today − 7·(level−1); keeps passed, theme, sidebar
def reset_course(delete_code):            # drops start + passed (keeps theme, sidebar); optionally removes work/
def current_level(progress, today=None):  # week whose span contains today (for the menu's ◉ mark)
def set_setting(key, value):              # theme / sidebar in progress.json
```

`progress.json` before Start or after Reset holds only preferences, e.g. `{"theme": "dark"}`. Every UI then shows the welcome screen when `"start"` is missing, instead of when the file is missing.

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
- The Reset dialog is a small `tk.Toplevel` with a `tk.Checkbutton`. `messagebox` can't hold a checkbox.
- On Windows the menu bar is native, and tk cannot recolour it in dark mode; it stays the system colour. Everything below it follows the theme as now.

**Web (`static/index.html` + `app.py`)**
- A slim HTML menu bar using `<details>` dropdowns (no library), styled with the existing CSS variables.
- Collapse with `body.collapsed nav { display: none }`; `main` is `flex: 1`, so it takes the space.
- New endpoints: `POST /api/start {level}`, `POST /api/level {level}`, `POST /api/reset {code}`. Confirmations are in-page dialogs, not `alert()`/`confirm()`.

## Steps (one commit each, pushed after each)

1. **`trainer.py`:** `start_course`, `reset_course`, `current_level`, `set_setting`; welcome-screen check based on `"start"`; CLI `start --level`, `level`, `reset [--code]`.
2. **GTK:** menu bar, Revealer sidebar with ☰ and Ctrl+B, level picker on the welcome screen, level and reset dialogs, theme moved to View.
3. **tkinter:** the same features.
4. **Web:** the same features plus the three endpoints.
5. **Docs:** README sections, and this plan marked done.
6. **Release v0.2.0:** bump `VERSION`, `make dist` + `build dist`, tag, GitHub release with notes.

## Testing

**`trainer.py`** (added to `selftest.py`):
- Level math: for N = 1…4 with a fixed `today`, the first unlocked day of week N is today. Weeks below N have all days and solutions unlocked. Week N+1 is still locked.
- Reset with and without `delete_code`: `start`/`passed` are gone, `theme`/`sidebar` stay, and `work/` is deleted only when asked.
- Everything runs in the temporary copy, as `selftest.py` already does. Your real `progress.json` is never touched.

**Windows**, driven by the existing harnesses (GTK offscreen, tkinter on Xvfb, web in Chrome) for each UI:
- Collapse via ☰, the menu and Ctrl+B. The statement + editor width grows by about the sidebar width (measured from widget sizes). Expanding restores the old width and scroll position.
- The collapsed state survives a restart.
- Start at level 3 from the welcome screen shows W3 Day 1 as today, and W1–W2 solutions are unlocked.
- Changing the level mid-course keeps the green dots.
- Reset → Cancel changes nothing. Reset → welcome screen keeps `work/` unless the box is ticked.
- The theme from the View menu still applies and persists.
- Screenshots in light and dark, collapsed and expanded.

## Size and risk

- About 300 lines across the four front ends plus about 60 in `trainer.py`. No new dependencies, and no change to the problem data.
- **`progress.json` format:** only new optional keys (`sidebar`); a v0.1.0 file keeps working.
- **Biggest behaviour change:** the welcome screen now depends on `"start"` rather than on whether the file exists. Step 1 updates every UI's check, and the tests cover it.
- **Not testable here:** Windows-only behaviour (the native menu bar look in `gui_tk.py`). Same caveat as v0.1.0.

## Open questions

1. **Lower levels when starting at level N:** open them fully for review (planned), or hide them?
2. **Reset:** offer "also delete my saved code" (planned, off by default), or never touch `work/`?
3. **Web app:** in scope (planned), or only the two desktop windows?
