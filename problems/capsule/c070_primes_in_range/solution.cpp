#include <iostream>

bool is_prime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int a, b, found = 0;
    std::cin >> a >> b;
    for (int x = a; x <= b; x++) {
        if (is_prime(x)) {
            if (found > 0) {
                std::cout << " ";
            }
            std::cout << x;
            found++;
        }
    }
    if (found == 0) {
        std::cout << "none\n";
    } else {
        std::cout << "\n";
    }
    return 0;
}
