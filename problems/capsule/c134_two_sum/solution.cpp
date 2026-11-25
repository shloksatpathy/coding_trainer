#include <iostream>
#include <unordered_map>
#include <vector>

int main() {
    int n;
    long long t;
    std::cin >> n >> t;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::unordered_map<long long, int> first;
    for (int j = 0; j < n; j++) {
        if (first.count(t - a[j])) {
            std::cout << first[t - a[j]] + 1 << " " << j + 1 << "\n";
            return 0;
        }
        if (first.count(a[j]) == 0) {
            first[a[j]] = j;
        }
    }
    std::cout << "none\n";
    return 0;
}
