#include <iostream>

int main() {
    int n, x;
    std::cin >> n >> x;
    int lo = x, hi = x;
    for (int i = 1; i < n; i++) {
        std::cin >> x;
        if (x < lo) {
            lo = x;
        }
        if (x > hi) {
            hi = x;
        }
    }
    std::cout << "min: " << lo << "\n";
    std::cout << "max: " << hi << "\n";
    return 0;
}
