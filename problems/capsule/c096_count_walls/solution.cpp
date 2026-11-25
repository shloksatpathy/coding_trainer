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
    int total = 0;
    for (int i = 0; i < r; i++) {
        int count = 0;
        for (int j = 0; j < c; j++) {
            if (g[i][j] == '#') {
                count++;
            }
        }
        std::cout << count << "\n";
        total += count;
    }
    std::cout << "total: " << total << "\n";
    return 0;
}
