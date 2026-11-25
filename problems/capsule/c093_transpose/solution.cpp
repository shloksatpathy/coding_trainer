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
        for (int i = 0; i < r; i++) {
            if (i > 0) {
                std::cout << " ";
            }
            std::cout << g[i][j];
        }
        std::cout << "\n";
    }
    return 0;
}
