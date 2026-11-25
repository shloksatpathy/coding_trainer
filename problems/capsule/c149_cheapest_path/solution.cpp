#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    int r, c;
    std::cin >> r >> c;
    std::vector<std::vector<long long>> g(r, std::vector<long long>(c)), best = g;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            std::cin >> g[i][j];
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (i == 0 && j == 0) {
                best[i][j] = g[i][j];
            } else if (i == 0) {
                best[i][j] = best[i][j - 1] + g[i][j];
            } else if (j == 0) {
                best[i][j] = best[i - 1][j] + g[i][j];
            } else {
                best[i][j] = std::min(best[i - 1][j], best[i][j - 1]) + g[i][j];
            }
        }
    }
    std::cout << best[r - 1][c - 1] << "\n";
    return 0;
}
