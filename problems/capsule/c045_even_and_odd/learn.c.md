**Learn · reading many values**

Call `scanf` once per value, inside a loop; it skips spaces and line breaks by itself.

```c
int n, x, total = 0;
scanf("%d", &n);
for (int i = 0; i < n; i++) {
    scanf("%d", &x);
    total += x;
}
printf("%d\n", total);
```

With the input `3` and `4 5 6` this prints the sum, `15`.
