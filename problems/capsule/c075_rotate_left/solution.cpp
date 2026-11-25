#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int k;
    std::cin >> k;
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << a[(i + k) % n];
    }
    std::cout << "\n";
    return 0;
}
