**Learn · splitting a line at commas**

In `scanf`, `%99[^,]` reads up to 99 characters that are not a comma; the `,` after it in the format skips the comma itself. A space at the start of the format skips the line break left over from the previous line.

```c
char name[100], city[100];
scanf(" %99[^,],%99s", name, city);
printf("%s\n", city);
```
