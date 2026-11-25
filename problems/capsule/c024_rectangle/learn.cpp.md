**Learn · reading decimal numbers**

`>>` reads a `double` just like an `int`.

```cpp
double price;
std::cin >> price;
std::cout << std::fixed << std::setprecision(2) << price * 2 << "\n";
```

With the input `1.25` this prints `2.50`.
