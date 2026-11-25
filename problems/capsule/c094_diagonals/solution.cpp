#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> g(n, std::vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cin >> g[i][j];
        }
    }
    int main_sum = 0, anti = 0;
    for (int i = 0; i < n; i++) {
        main_sum += g[i][i];
        anti += g[i][n - 1 - i];
    }
    std::cout << "main: " << main_sum << "\n";
    std::cout << "anti: " << anti << "\n";
    return 0;
}
