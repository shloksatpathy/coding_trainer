#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if (n > 0) {
        std::cout << "positive\n";
    } else if (n < 0) {
        std::cout << "negative\n";
    } else {
        std::cout << "zero\n";
    }
    return 0;
}
