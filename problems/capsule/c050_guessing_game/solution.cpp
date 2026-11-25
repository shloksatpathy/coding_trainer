#include <iostream>

int main() {
    int secret, n, g;
    std::cin >> secret >> n;
    bool found = false;
    for (int k = 1; k <= n; k++) {
        std::cin >> g;
        if (g < secret) {
            std::cout << "too low\n";
        } else if (g > secret) {
            std::cout << "too high\n";
        } else {
            std::cout << "correct on guess " << k << "\n";
            found = true;
            break;
        }
    }
    if (!found) {
        std::cout << "no luck, it was " << secret << "\n";
    }
    return 0;
}
