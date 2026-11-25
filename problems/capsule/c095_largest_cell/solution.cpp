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
    int best = g[0][0], br = 0, bc = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (g[i][j] > best) {
                best = g[i][j];
                br = i;
                bc = j;
            }
        }
    }
    std::cout << "max: " << best << " at " << br + 1 << " " << bc + 1 << "\n";
    return 0;
}
