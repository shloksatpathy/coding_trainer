**Learn · reading many values**

Use `>>` once per value, inside a loop; it skips spaces and line breaks by itself.

```cpp
int n, x, total = 0;
std::cin >> n;
for (int i = 0; i < n; i++) {
    std::cin >> x;
    total += x;
}
std::cout << total << "\n";
```

With the input `3` and `4 5 6` this prints the sum, `15`.
