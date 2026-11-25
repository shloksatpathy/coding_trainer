#include <iostream>
#include <string>
#include <vector>

int main() {
    int r, c;
    std::cin >> r >> c;
    std::vector<std::string> g(r);
    for (int i = 0; i < r; i++) {
        std::cin >> g[i];
    }
    for (int j = 0; j < c; j++) {
        for (int k = 0; k < r; k++) {
            std::cout << g[r - 1 - k][j];
        }
        std::cout << "\n";
    }
    return 0;
}
