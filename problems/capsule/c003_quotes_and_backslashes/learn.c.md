**Learn · escapes**

A `"` would end the text, so inside quotes you write `\"` for a quote. A `\` starts an escape (like `\n`), so you write `\\` for one backslash.

```c
printf("A \"quoted\" word\n");
printf("one\\two\n");
```

prints `A "quoted" word` and `one\two`.
