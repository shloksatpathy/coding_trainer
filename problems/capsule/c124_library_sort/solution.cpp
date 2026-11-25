#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::sort(a.begin(), a.end());
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << a[i];
    }
    std::cout << "\n";
    std::sort(a.begin(), a.end(), std::greater<int>());
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << a[i];
    }
    std::cout << "\n";
    return 0;
}
