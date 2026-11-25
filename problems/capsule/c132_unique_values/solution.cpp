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
    std::vector<long long> out;
    for (int i = 0; i < n; i++) {
        if (seen.count(a[i]) == 0) {
            seen.insert(a[i]);
            out.push_back(a[i]);
        }
    }
    for (std::size_t i = 0; i < out.size(); i++) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << out[i];
    }
    std::cout << "\ndistinct: " << out.size() << "\n";
    return 0;
}
