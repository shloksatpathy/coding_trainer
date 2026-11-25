#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int k = 1; k <= 2 * n - 1; k++) {
        int i;
        if (k <= n) {
            i = k;
        } else {
            i = 2 * n - k;
        }
        for (int j = 0; j < n - i; j++) {
            std::cout << " ";
        }
        for (int j = 0; j < 2 * i - 1; j++) {
            std::cout << "*";
        }
        std::cout << "\n";
    }
    return 0;
}
