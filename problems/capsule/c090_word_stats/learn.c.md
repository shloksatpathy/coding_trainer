**Learn · keeping a copy of a word**

`=` can't copy an array. `strcpy(dest, src)` (from `<string.h>`) copies the text of `src` into `dest`, which must have room for it.

```c
char best[100], w[100];
while (scanf("%99s", w) == 1) {
    strcpy(best, w);
}
printf("%s\n", best);
```

keeps the last word.
