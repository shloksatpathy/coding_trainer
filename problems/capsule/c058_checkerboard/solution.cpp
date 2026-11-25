#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int r = 0; r < n; r++) {
        for (int col = 0; col < n; col++) {
            if ((r + col) % 2 == 0) {
                std::cout << "#";
            } else {
                std::cout << ".";
            }
        }
        std::cout << "\n";
    }
    return 0;
}
