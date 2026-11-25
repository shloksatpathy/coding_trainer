#include <iostream>

void binary(int n) {
    if (n >= 2) {
        binary(n / 2);
    }
    std::cout << n % 2;
}

int main() {
    int n;
    std::cin >> n;
    binary(n);
    std::cout << "\n";
    return 0;
}
