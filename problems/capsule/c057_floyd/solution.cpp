#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int k = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (j > 0) {
                std::cout << " ";
            }
            std::cout << k;
            k++;
        }
        std::cout << "\n";
    }
    return 0;
}
