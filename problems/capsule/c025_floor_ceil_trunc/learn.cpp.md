**Learn · decimal to whole number**

`std::floor` and `std::ceil` come from `<cmath>` and still return a `double`. `(int)x` converts to `int` by cutting off the fraction, which rounds toward zero.

```cpp
double x = -3.5;
std::cout << (int)std::floor(x) << " " << (int)std::ceil(x) << " " << (int)x << "\n";
```

prints `-4 -3 -3`.
