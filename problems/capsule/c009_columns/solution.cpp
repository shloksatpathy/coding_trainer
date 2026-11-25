#include <iomanip>
#include <iostream>

int main() {
    std::cout << std::left << std::setw(10) << "Item" << std::right << std::setw(5) << "Qty" << "\n";
    std::cout << std::left << std::setw(10) << "apple" << std::right << std::setw(5) << 3 << "\n";
    std::cout << std::left << std::setw(10) << "banana" << std::right << std::setw(5) << 12 << "\n";
    std::cout << std::left << std::setw(10) << "cherry" << std::right << std::setw(5) << 150 << "\n";
    return 0;
}
