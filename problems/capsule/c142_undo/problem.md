# C142 · Undo

The first line has `n`; each of the next `n` lines is a command: `add WORD` appends a word to the text, `undo` removes the most recently added word that is still there (nothing happens if there is none), and `show` prints the current words separated by spaces, or `(empty)`.

**Example**

Input (also in `in.txt`):
```
6
add hello
add world
show
undo
show
undo
```
Output:
```
hello world
hello
```

**Focus:** undo history is a stack of changes.
