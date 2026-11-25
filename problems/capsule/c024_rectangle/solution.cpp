#include <iomanip>
#include <iostream>

int main() {
    double w, h;
    std::cin >> w >> h;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "area: " << w * h << "\n";
    std::cout << "perimeter: " << 2 * (w + h) << "\n";
    return 0;
}
