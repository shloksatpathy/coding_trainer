#include <iostream>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    if (a <= 0 || b <= 0 || c <= 0 || a + b <= c || a + c <= b || b + c <= a) {
        std::cout << "not a triangle\n";
    } else if (a == b && b == c) {
        std::cout << "equilateral\n";
    } else if (a == b || b == c || a == c) {
        std::cout << "isosceles\n";
    } else {
        std::cout << "scalene\n";
    }
    return 0;
}
