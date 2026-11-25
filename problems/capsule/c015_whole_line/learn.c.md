**Learn · reading a whole line**

`%s` stops at the first space. `fgets` reads the whole line, including its line break; `strcspn` (from `<string.h>`) finds the line break so you can cut it off with `'\0'`, the end-of-text mark.

```c
char line[200];
fgets(line, sizeof line, stdin);
line[strcspn(line, "\n")] = '\0';
printf("[%s]\n", line);
```
