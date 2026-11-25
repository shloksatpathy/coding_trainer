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
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (g[i][j] == '*') {
                std::cout << "*";
                continue;
            }
            int count = 0;
            for (int di = -1; di <= 1; di++) {
                for (int dj = -1; dj <= 1; dj++) {
                    int ni = i + di, nj = j + dj;
                    if (ni >= 0 && ni < r && nj >= 0 && nj < c && g[ni][nj] == '*') {
                        count++;
                    }
                }
            }
            std::cout << count;
        }
        std::cout << "\n";
    }
    return 0;
}
