#include <iomanip>
#include <iostream>

int main() {
    int total, count;
    std::cin >> total >> count;
    std::cout << "whole: " << total / count << "\n";
    std::cout << std::fixed << std::setprecision(3) << "exact: " << static_cast<double>(total) / count << "\n";
    return 0;
}
