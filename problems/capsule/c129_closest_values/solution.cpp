#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::sort(a.begin(), a.end());
    long long best = (long long)a[1] - a[0];
    for (int i = 2; i < n; i++) {
        if ((long long)a[i] - a[i - 1] < best) {
            best = (long long)a[i] - a[i - 1];
        }
    }
    std::cout << best << "\n";
    return 0;
}
