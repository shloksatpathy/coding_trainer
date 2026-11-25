#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int k = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || a[i] != a[i - 1]) {
            if (k > 0) {
                std::cout << " ";
            }
            std::cout << a[i];
            k++;
        }
    }
    std::cout << "\ndistinct: " << k << "\n";
    return 0;
}
