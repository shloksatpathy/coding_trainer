#include <iostream>
#include <vector>

int total(const std::vector<int> &a, std::size_t i) {
    if (i == a.size()) {
        return 0;
    }
    return a[i] + total(a, i + 1);
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::cout << total(a, 0) << "\n";
    return 0;
}
