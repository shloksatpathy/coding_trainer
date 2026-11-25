#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int digits = 1;
    while (n >= 10) {
        n /= 10;
        digits++;
    }
    std::cout << digits << "\n";
    return 0;
}
