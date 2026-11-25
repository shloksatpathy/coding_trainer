#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= 10; i++) {
        if (i > 1) {
            std::cout << " ";
        }
        std::cout << n * i;
    }
    std::cout << "\n";
    return 0;
}
