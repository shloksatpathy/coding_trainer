# P38 · Evaluate postfix expressions

Read a postfix (Reverse Polish) expression: integer tokens (possibly negative, like `-3`) and operators `+ - * /`, separated by spaces. Print its value. `/` truncates toward zero. The expression is always valid and never divides by zero.

Sample: `2 3 1 * + 9 -` → `-4`

**Focus:** a stack of numbers; the operator pops `b` first, then `a`, and pushes `a op b`. Telling `-3` from `-` is the parsing trap. Python: remember `//` floors.

**Sample input** (also in `in.txt`):
```
2 3 1 * + 9 -
```
