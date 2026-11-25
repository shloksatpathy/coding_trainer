#include <iostream>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    int best = a;
    if (b > best) {
        best = b;
    }
    if (c > best) {
        best = c;
    }
    std::cout << best << "\n";
    return 0;
}
