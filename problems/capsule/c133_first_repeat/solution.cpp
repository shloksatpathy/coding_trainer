#include <iostream>
#include <unordered_set>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::unordered_set<long long> seen;
    for (int i = 0; i < n; i++) {
        if (seen.count(a[i])) {
            std::cout << a[i] << "\n";
            return 0;
        }
        seen.insert(a[i]);
    }
    std::cout << "none\n";
    return 0;
}
