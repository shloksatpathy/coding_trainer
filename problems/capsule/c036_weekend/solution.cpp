#include <iostream>

int main() {
    int d;
    std::cin >> d;
    if (d == 6 || d == 7) {
        std::cout << "weekend\n";
    } else if (d >= 1 && d <= 5) {
        std::cout << "weekday\n";
    } else {
        std::cout << "invalid\n";
    }
    return 0;
}
