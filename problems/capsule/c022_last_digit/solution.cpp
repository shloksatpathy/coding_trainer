#include <iostream>

int main() {
    int n;
    std::cin >> n;
    std::cout << "last digit: " << n % 10 << "\n";
    std::cout << "without it: " << n / 10 << "\n";
    return 0;
}
