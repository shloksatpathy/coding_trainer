#include <iostream>

int main() {
    int x, y;
    std::cin >> x >> y;
    if (x == 0 && y == 0) {
        std::cout << "origin\n";
    } else if (y == 0) {
        std::cout << "x-axis\n";
    } else if (x == 0) {
        std::cout << "y-axis\n";
    } else if (x > 0) {
        if (y > 0) {
            std::cout << "Q1\n";
        } else {
            std::cout << "Q4\n";
        }
    } else {
        if (y > 0) {
            std::cout << "Q2\n";
        } else {
            std::cout << "Q3\n";
        }
    }
    return 0;
}
