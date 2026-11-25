#include <iostream>
#include <unordered_map>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::unordered_map<long long, int> count;
    for (int i = 0; i < n; i++) {
        count[a[i]]++;
    }
    long long best = a[0];
    int best_count = 0;
    for (auto &entry : count) {
        if (entry.second > best_count || (entry.second == best_count && entry.first < best)) {
            best = entry.first;
            best_count = entry.second;
        }
    }
    std::cout << "value: " << best << "\n";
    std::cout << "count: " << best_count << "\n";
    std::cout << "distinct: " << count.size() << "\n";
    return 0;
}
