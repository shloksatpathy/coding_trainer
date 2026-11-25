#include <iomanip>
#include <iostream>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    std::cout << std::fixed << std::setprecision(2) << (a + b + c) / 3.0 << "\n";
    return 0;
}
