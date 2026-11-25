**Learn · grids**

A `std::vector` of `std::vector<int>` rows: `std::vector<std::vector<int>> g(r, std::vector<int>(c));` makes `r` rows of `c` zeros. `g[i][j]` is row `i`, column `j`, both counting from 0.

```cpp
std::vector<std::vector<int>> g = {{1, 2, 3}, {4, 5, 6}};
std::cout << g[1][0] << "\n";
```

prints `4`: row 1, column 0.
