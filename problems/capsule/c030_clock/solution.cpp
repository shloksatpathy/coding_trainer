#include <iomanip>
#include <iostream>

int main() {
    int s;
    std::cin >> s;
    std::cout << s / 3600 << ":" << std::setfill('0') << std::setw(2) << s / 60 % 60 << ":" << std::setw(2) << s % 60 << "\n";
    return 0;
}
