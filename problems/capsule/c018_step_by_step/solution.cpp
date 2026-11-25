#include <iostream>

int main() {
    int x;
    std::cin >> x;
    std::cout << "start: " << x << "\n";
    x += 5;
    std::cout << "+5: " << x << "\n";
    x *= 2;
    std::cout << "*2: " << x << "\n";
    x -= 3;
    std::cout << "-3: " << x << "\n";
    return 0;
}
