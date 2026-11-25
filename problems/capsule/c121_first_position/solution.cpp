#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int q, x;
    std::cin >> q;
    for (int k = 0; k < q; k++) {
        std::cin >> x;
        int pos = -1;
        for (int i = 0; i < n; i++) {
            if (a[i] == x) {
                pos = i + 1;
                break;
            }
        }
        std::cout << pos << "\n";
    }
    return 0;
}
