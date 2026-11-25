**Learn · big whole numbers**

An `int` holds values up to 2 147 483 647; past that it overflows and gives wrong results. `long long` holds up to about 9.2 × 10^18; read and print it with `%lld`. The `LL` suffix makes a number `long long`.

```c
long long big = 1000000000LL * 1000000000LL;
printf("%lld\n", big);
```

prints `1000000000000000000`.
