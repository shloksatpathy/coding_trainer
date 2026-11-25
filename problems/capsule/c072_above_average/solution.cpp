#include <iomanip>
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int total = 0, found = 0;
    for (int i = 0; i < n; i++) {
        total += a[i];
    }
    std::cout << std::fixed << std::setprecision(2) << "average: " << (double)total / n << "\n";
    for (int i = 0; i < n; i++) {
        if (a[i] * n > total) {
            if (found > 0) {
                std::cout << " ";
            }
            std::cout << a[i];
            found++;
        }
    }
    if (found == 0) {
        std::cout << "none\n";
    } else {
        std::cout << "\n";
    }
    return 0;
}
