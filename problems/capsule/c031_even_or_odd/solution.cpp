#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if (n % 2 == 0) {
        std::cout << "even\n";
    } else {
        std::cout << "odd\n";
    }
    return 0;
}
