#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if (n >= 1 && n <= 100) {
        std::cout << "inside\n";
    } else {
        std::cout << "outside\n";
    }
    return 0;
}
