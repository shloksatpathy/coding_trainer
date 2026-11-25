# C143 · Queue

The first line has `n`; each of the next `n` lines is `join NAME` (that person joins the end of the queue) or `serve` (print `served NAME` for the person at the front and remove them, or `nobody waiting`). At the end print `waiting: …` with the names still in the queue, front first, or `waiting: none`.

**Example**

Input (also in `in.txt`):
```
6
join ann
join bob
serve
join cy
serve
serve
```
Output:
```
served ann
served bob
served cy
waiting: none
```

**Focus:** a queue: first in, first out. An array plus the index of the front does it without moving anything.
