#include <iostream>
#include <string>

int main() {
    std::string name, city;
    int year;
    std::cin >> name >> city >> year;
    std::cout << name << " from " << city << ", since " << year << "\n";
    std::cout << "That is " << 2026 - year << " years before 2026.\n";
    return 0;
}
