**Learn · leading zeros**

`std::setfill('0')` (it stays on) and `std::setw(2)` (only for the next value) pad with zeros to 2 digits.

```cpp
std::cout << std::setfill('0') << std::setw(2) << 7 << "\n";
```

prints `07`.
