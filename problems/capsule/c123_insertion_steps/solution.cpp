#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    for (int i = 1; i < n; i++) {
        int x = a[i], j = i - 1;
        while (j >= 0 && a[j] > x) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = x;
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                std::cout << " ";
            }
            std::cout << a[i];
        }
        std::cout << "\n";
    }
    return 0;
}
