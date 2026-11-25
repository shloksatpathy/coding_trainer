**Learn · converting a whole number to a decimal**

`int / int` is whole-number division. Convert one side first: `static_cast<double>(n) / 2` (or `(double)n / 2`) is decimal division.

```cpp
int n = 7;
std::cout << n / 2 << " " << static_cast<double>(n) / 2 << "\n";
```

prints `3 3.5`.
