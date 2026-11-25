**Learn · decimal numbers**

`double` holds a decimal number. Dividing by `2.0` (a decimal) makes the whole division decimal. `std::fixed << std::setprecision(2)` (from `<iomanip>`) prints 2 decimals from then on.

```cpp
double half = 7 / 2.0;
std::cout << std::fixed << std::setprecision(2) << half << "\n";
```

prints `3.50`.
