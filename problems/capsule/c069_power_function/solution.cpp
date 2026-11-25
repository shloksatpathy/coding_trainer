#include <iostream>

long long power(long long base, int exp) {
    long long result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main() {
    long long base;
    int exp;
    std::cin >> base >> exp;
    std::cout << power(base, exp) << "\n";
    return 0;
}
