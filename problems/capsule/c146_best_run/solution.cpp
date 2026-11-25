#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    long long here = a[0], best = a[0];
    for (int i = 1; i < n; i++) {
        if (here > 0) {
            here += a[i];
        } else {
            here = a[i];
        }
        if (here > best) {
            best = here;
        }
    }
    std::cout << best << "\n";
    return 0;
}
