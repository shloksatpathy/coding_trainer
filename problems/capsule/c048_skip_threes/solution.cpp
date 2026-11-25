#include <iostream>

int main() {
    int n;
    std::cin >> n;
    bool first = true;
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0) {
            continue;
        }
        if (!first) {
            std::cout << " ";
        }
        std::cout << i;
        first = false;
    }
    std::cout << "\n";
    return 0;
}
