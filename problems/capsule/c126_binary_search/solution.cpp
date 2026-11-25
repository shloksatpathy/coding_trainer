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
        int lo = 0, hi = n - 1, pos = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] == x) {
                pos = mid + 1;
                break;
            }
            if (a[mid] < x) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        std::cout << pos << "\n";
    }
    return 0;
}
