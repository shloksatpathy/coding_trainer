**Learn · sorted sets and set operations**

`std::set<int>` (from `<set>`) keeps its values sorted and unique, and `for (int x : s)` visits them in order.

```cpp
std::set<int> s = {3, 1, 3, 2};
for (int x : s) {
    std::cout << x << " ";
}
```
