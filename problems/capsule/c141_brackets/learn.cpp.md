**Learn · stacks**

A `std::vector` works as a stack: `push_back(x)`, `back()` is the top, `pop_back()` removes it, `empty()` checks.

```cpp
std::vector<int> s;
s.push_back(1);
s.push_back(2);
std::cout << s.back() << "\n";
s.pop_back();
```

The last value pushed comes off first.
