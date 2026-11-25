**Learn · words**

`%s` skips spaces and reads one word. `scanf` returns how many values it read, so `while (scanf("%99s", w) == 1)` reads word after word until the input runs out.

```c
char w[100];
while (scanf("%99s", w) == 1) {
    printf("%s\n", w);
}
```

With the input `  to be  ` this prints `to` and `be` on two lines.
