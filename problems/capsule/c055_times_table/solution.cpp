#include <iomanip>
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int r = 1; r <= n; r++) {
        for (int col = 1; col <= n; col++) {
            std::cout << std::setw(4) << r * col;
        }
        std::cout << "\n";
    }
    return 0;
}
