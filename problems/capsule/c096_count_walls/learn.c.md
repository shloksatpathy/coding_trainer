**Learn · a grid of characters**

Each row is a `char` array with room for the end-of-text mark: `char g[100][101];` and `scanf("%100s", g[i])` reads row `i`. Then `g[i][j]` is a character; compare it with `'#'` (single quotes for one character).

```c
char g[2][3] = {"#.", ".#"};
printf("%d\n", g[1][1] == '#');
```

prints that the bottom-right character is a wall.
