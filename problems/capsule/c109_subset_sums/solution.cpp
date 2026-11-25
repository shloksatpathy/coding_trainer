#include <iostream>
#include <vector>

int count(const std::vector<int> &a, std::size_t i, int left) {
    if (i == a.size()) {
        if (left == 0) {
            return 1;
        }
        return 0;
    }
    return count(a, i + 1, left) + count(a, i + 1, left - a[i]);
}

int main() {
    int n, t;
    std::cin >> n >> t;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::cout << count(a, 0, t) << "\n";
    return 0;
}
