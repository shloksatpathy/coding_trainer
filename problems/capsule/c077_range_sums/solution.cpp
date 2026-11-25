#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::vector<int> p(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        p[i] = p[i - 1] + a[i - 1];
    }
    int q, l, r;
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> l >> r;
        std::cout << p[r] - p[l - 1] << "\n";
    }
    return 0;
}
