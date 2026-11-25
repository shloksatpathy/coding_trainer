**Learn · decimal to whole number**

`floor` and `ceil` come from `<math.h>` and still return a `double`. `(int)x` converts to `int` by cutting off the fraction, which rounds toward zero.

```c
double x = -3.5;
printf("%d %d %d\n", (int)floor(x), (int)ceil(x), (int)x);
```

prints `-4 -3 -3`.
