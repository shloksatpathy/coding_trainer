#include <iostream>

bool is_between(int x, int lo, int hi) {
    return lo <= x && x <= hi;
}

int main() {
    int lo, hi, n, x;
    std::cin >> lo >> hi >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> x;
        if (is_between(x, lo, hi)) {
            std::cout << "yes\n";
        } else {
            std::cout << "no\n";
        }
    }
    return 0;
}
