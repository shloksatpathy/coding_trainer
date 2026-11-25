#include <iostream>

int digit_sum(int n) {
    if (n < 10) {
        return n;
    }
    return n % 10 + digit_sum(n / 10);
}

int main() {
    int n;
    std::cin >> n;
    std::cout << digit_sum(n) << "\n";
    return 0;
}
