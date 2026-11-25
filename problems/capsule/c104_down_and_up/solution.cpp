#include <iostream>

void down_up(int n) {
    if (n == 0) {
        return;
    }
    std::cout << n << "\n";
    down_up(n - 1);
    std::cout << n << "\n";
}

int main() {
    int n;
    std::cin >> n;
    down_up(n);
    return 0;
}
