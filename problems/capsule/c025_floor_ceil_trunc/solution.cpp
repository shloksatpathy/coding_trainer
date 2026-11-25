#include <cmath>
#include <iostream>

int main() {
    double x;
    std::cin >> x;
    std::cout << (int)std::floor(x) << " " << (int)std::ceil(x) << " " << (int)x << "\n";
    return 0;
}
