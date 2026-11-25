**Learn · reading values with separators**

Characters in the `scanf` format must appear in the input: `scanf("%d:%d", &h, &m)` reads `09:15`.

```c
int h, m;
scanf("%d:%d", &h, &m);
printf("%d %d\n", h, m);
```

prints `9 15`.
