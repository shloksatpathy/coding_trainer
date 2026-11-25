#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += a[i];
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << total;
    }
    std::cout << "\n";
    return 0;
}
