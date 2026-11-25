#include <iostream>

int main() {
    int coins[8] = {200, 100, 50, 20, 10, 5, 2, 1};
    int amount, total = 0;
    std::cin >> amount;
    for (int i = 0; i < 8; i++) {
        int k = amount / coins[i];
        if (k > 0) {
            std::cout << coins[i] << " x " << k << "\n";
            amount -= k * coins[i];
            total += k;
        }
    }
    std::cout << "coins: " << total << "\n";
    return 0;
}
