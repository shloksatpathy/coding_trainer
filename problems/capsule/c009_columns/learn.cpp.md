**Learn · fixed widths**

`#include <iomanip>` gives `std::setw(n)`, which pads the next value to n characters. `std::left` and `std::right` choose the side.

```cpp
std::cout << std::left << std::setw(8) << "pear" << "|"
          << std::right << std::setw(4) << 7 << "|\n";
```

prints `pear    |   7|`.
