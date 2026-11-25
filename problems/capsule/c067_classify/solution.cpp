#include <iostream>
#include <string>

std::string classify(int n) {
    if (n < 0) {
        return "negative";
    }
    if (n == 0) {
        return "zero";
    }
    if (n < 10) {
        return "small";
    }
    if (n < 100) {
        return "medium";
    }
    return "large";
}

int main() {
    int n, x;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> x;
        std::cout << classify(x) << "\n";
    }
    return 0;
}
