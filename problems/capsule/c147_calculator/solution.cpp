#include <iostream>

int main() {
    long long total = 0, term, x;
    char op;
    std::cin >> term;
    while (std::cin >> op >> x) {
        if (op == '*') {
            term *= x;
        } else {
            total += term;
            if (op == '+') {
                term = x;
            } else {
                term = -x;
            }
        }
    }
    std::cout << total + term << "\n";
    return 0;
}
