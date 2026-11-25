#include <iostream>

int absolute(int x) {
    if (x < 0) {
        return -x;
    }
    return x;
}

int distance(int a, int b) {
    return absolute(a - b);
}

int main() {
    int n, a, b;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> a >> b;
        std::cout << distance(a, b) << "\n";
    }
    return 0;
}
