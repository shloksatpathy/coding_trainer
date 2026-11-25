#include <iostream>

int max2(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int max3(int a, int b, int c) {
    return max2(max2(a, b), c);
}

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    std::cout << max3(a, b, c) << "\n";
    return 0;
}
