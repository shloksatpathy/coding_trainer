**Learn · returning early, returning text**

A `return` ends the function at once, so the checks after it need no `else`. A function can return fixed text as `const char *` (a pointer to the text; pointers come later) and you print it with `%s`.

```c
const char *size(int n) {
    if (n < 10) {
        return "short";
    }
    return "long";
}
```
