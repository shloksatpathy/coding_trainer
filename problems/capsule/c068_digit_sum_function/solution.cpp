#include <iostream>

int digit_sum(int n) {
    int s = 0;
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

int main() {
    int n, x, best = -1, best_sum = -1;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> x;
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << digit_sum(x);
        if (digit_sum(x) > best_sum) {
            best_sum = digit_sum(x);
            best = x;
        }
    }
    std::cout << "\nbest: " << best << "\n";
    return 0;
}
