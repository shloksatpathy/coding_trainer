#include <iostream>
#include <vector>

int main() {
    int n, t;
    std::cin >> n >> t;
    std::vector<int> a(n);
    for (int k = 0; k < n; k++) {
        std::cin >> a[k];
    }
    int i = 0, j = n - 1, found = 0;
    while (i < j) {
        int s = a[i] + a[j];
        if (s == t) {
            std::cout << a[i] << " " << a[j] << "\n";
            found++;
            i++;
            j--;
        } else if (s < t) {
            i++;
        } else {
            j--;
        }
    }
    if (found == 0) {
        std::cout << "none\n";
    }
    return 0;
}
