**Learn · looking at each character**

Loop until the end-of-text mark `'\0'`. `<ctype.h>` has `isupper`, `islower`, `isdigit` to test a character and `toupper`, `tolower` to convert it.

```c
char text[] = "a1B";
for (int i = 0; text[i] != '\0'; i++) {
    if (isupper(text[i])) {
        printf("%c is uppercase\n", text[i]);
    }
}
```

prints `B is uppercase`.
