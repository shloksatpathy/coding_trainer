# C141 · Balanced brackets

Read one line of text. Print `yes` if its brackets `()`, `[]` and `{}` are balanced (every opening bracket is closed by the matching kind, in the right order) and `no` otherwise. Other characters are ignored.

**Example**

Input (also in `in.txt`):
```
([]{})
```
Output:
```
yes
```

**Focus:** a stack: the last bracket opened is the first one that must be closed.
