**Learn · arrays and lists**

`std::vector<int> a(n);` (from `<vector>`) holds `n` `int`s; `a[i]` is the one at position `i` (counting from 0) and `a.size()` is the count.

```cpp
int n;
std::cin >> n;
std::vector<int> a(n);
for (int i = 0; i < n; i++) {
    std::cin >> a[i];
}
std::cout << a[0] << " " << a.size() << "\n";
```

With the input `3` and `7 8 9` this prints `7 3`.
