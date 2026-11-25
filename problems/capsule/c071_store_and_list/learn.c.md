**Learn · arrays and lists**

An array holds many values of one type: `int a[1000];` has room for 1000 `int`s and `a[i]` is the one at position `i` (counting from 0). C doesn't check the positions you use: stay inside the size.

```c
int n;
int a[1000];
scanf("%d", &n);
for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
}
printf("%d %d\n", a[0], n);
```

With the input `3` and `7 8 9` this prints `7 3`.
