**Learn · reading text**

Text is stored in a `char` array. `%s` reads one word into it (no `&` for arrays); `%99s` reads at most 99 characters, so the word always fits in 100.

```c
char city[100];
scanf("%99s", city);
printf("I live in %s\n", city);
```
