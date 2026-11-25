**Learn · sorting numbers with the library**

`std::sort(a.begin(), a.end())` from `<algorithm>` sorts from small to large; pass `std::greater<int>()` (from `<functional>`) as a third argument to sort from large to small.

```cpp
std::vector<int> a = {3, 1, 2};
std::sort(a.begin(), a.end());
```
