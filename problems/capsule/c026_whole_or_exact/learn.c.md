**Learn · converting a whole number to a decimal**

`int / int` is whole-number division. Convert one side first: `(double)n / 2` is decimal division.

```c
int n = 7;
printf("%d %.1f\n", n / 2, (double)n / 2);
```

prints `3 3.5`.
