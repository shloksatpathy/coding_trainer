**Learn · big whole numbers**

An `int` holds values up to 2 147 483 647; past that it overflows and gives wrong results. `long long` holds up to about 9.2 × 10^18. The `LL` suffix makes a number `long long`.

```cpp
long long big = 1000000000LL * 1000000000LL;
std::cout << big << "\n";
```

prints `1000000000000000000`.
