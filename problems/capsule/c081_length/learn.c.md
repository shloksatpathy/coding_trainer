**Learn · length of text**

`strlen(text)` (from `<string.h>`) counts the characters before the end-of-text mark `'\0'`. It returns a `size_t`, printed with `%zu`.

```c
char name[] = "Ada";
printf("%zu\n", strlen(name));
```

prints `3`.
