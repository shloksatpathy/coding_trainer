#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    int q = a / b;
    int r = a % b;
    std::cout << "a / b = " << q << "\n";
    std::cout << "a % b = " << r << "\n";
    std::cout << "Q * b + R = " << q * b + r << "\n";
    return 0;
}
