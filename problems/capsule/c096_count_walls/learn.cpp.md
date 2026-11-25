**Learn · a grid of characters**

A `std::vector<std::string>` holds the rows; `std::cin >> g[i]` reads row `i`. Then `g[i][j]` is a character; compare it with `'#'` (single quotes for one character).

```cpp
std::vector<std::string> g = {"#.", ".#"};
std::cout << (g[1][1] == '#') << "\n";
```

prints that the bottom-right character is a wall.
