#include <iostream>

int square(int x) {
    return x * x;
}

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << square(a) + square(b) << "\n";
    return 0;
}
