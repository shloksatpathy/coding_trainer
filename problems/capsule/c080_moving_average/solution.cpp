#include <iomanip>
#include <iostream>
#include <vector>

int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int window = 0;
    for (int i = 0; i < k; i++) {
        window += a[i];
    }
    std::cout << std::fixed << std::setprecision(2) << (double)window / k;
    for (int i = k; i < n; i++) {
        window += a[i] - a[i - k];
        std::cout << " " << (double)window / k;
    }
    std::cout << "\n";
    return 0;
}
