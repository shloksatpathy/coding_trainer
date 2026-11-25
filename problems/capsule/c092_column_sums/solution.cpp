#include <iostream>
#include <vector>

int main() {
    int r, c;
    std::cin >> r >> c;
    std::vector<std::vector<int>> g(r, std::vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            std::cin >> g[i][j];
        }
    }
    for (int j = 0; j < c; j++) {
        int total = 0;
        for (int i = 0; i < r; i++) {
            total += g[i][j];
        }
        if (j > 0) {
            std::cout << " ";
        }
        std::cout << total;
    }
    std::cout << "\n";
    return 0;
}
