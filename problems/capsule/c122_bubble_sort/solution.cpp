#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int swaps = 0;
    bool swapped = true;
    while (swapped) {
        swapped = false;
        for (int i = 0; i < n - 1; i++) {
            if (a[i] > a[i + 1]) {
                int t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
                swaps++;
                swapped = true;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << a[i];
    }
    std::cout << "\n";
    std::cout << "swaps: " << swaps << "\n";
    return 0;
}
