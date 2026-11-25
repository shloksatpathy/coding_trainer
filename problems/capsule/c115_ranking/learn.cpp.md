**Learn · sorting with your own rule**

`std::sort(v.begin(), v.end(), before)` from `<algorithm>` sorts with your function `before(a, b)`, which returns true when `a` must come before `b`. `std::string`s compare alphabetically with `<`.

```cpp
bool longer(const std::string &a, const std::string &b) {
    return a.size() > b.size();
}

// std::sort(words.begin(), words.end(), longer);
```
