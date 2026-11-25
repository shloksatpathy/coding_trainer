#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int r = 0; r < n; r++) {
        for (int col = 0; col < n; col++) {
            if (r == 0 || r == n - 1 || col == 0 || col == n - 1) {
                std::cout << "#";
            } else {
                std::cout << " ";
            }
        }
        std::cout << "\n";
    }
    return 0;
}
