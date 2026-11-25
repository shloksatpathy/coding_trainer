#include <iostream>

int main() {
    int n, x, even = 0, odd = 0;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> x;
        if (x % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
    std::cout << "even: " << even << "\n";
    std::cout << "odd: " << odd << "\n";
    return 0;
}
