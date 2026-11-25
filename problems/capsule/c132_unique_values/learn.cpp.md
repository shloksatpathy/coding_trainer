**Learn · sets**

`std::unordered_set<long long>` (from `<unordered_set>`) holds each value at most once: `s.insert(x)`, `s.count(x)` is 1 when `x` is in it.

```cpp
std::unordered_set<long long> s;
s.insert(4);
s.insert(4);
std::cout << s.size() << " " << s.count(4) << "\n";
```
