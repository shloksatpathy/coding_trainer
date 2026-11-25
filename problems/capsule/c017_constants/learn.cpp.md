**Learn · constants**

`const` makes a variable read-only: assigning to it again is a compile error.

```cpp
const int HOURS_PER_DAY = 24;
int days;
std::cin >> days;
std::cout << days * HOURS_PER_DAY << "\n";
```
