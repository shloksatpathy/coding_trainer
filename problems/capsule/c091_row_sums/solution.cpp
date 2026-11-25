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
    for (int i = 0; i < r; i++) {
        int total = 0;
        for (int j = 0; j < c; j++) {
            if (j > 0) {
                std::cout << " ";
            }
            std::cout << g[i][j];
            total += g[i][j];
        }
        std::cout << " | " << total << "\n";
    }
    return 0;
}
