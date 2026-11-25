#include <iostream>
#include <vector>

int main() {
    int n, m;
    std::cin >> n;
    std::vector<int> a(n);
    for (int k = 0; k < n; k++) {
        std::cin >> a[k];
    }
    std::cin >> m;
    std::vector<int> b(m);
    for (int k = 0; k < m; k++) {
        std::cin >> b[k];
    }
    int i = 0, j = 0;
    for (int k = 0; k < n + m; k++) {
        if (k > 0) {
            std::cout << " ";
        }
        if (j == m || (i < n && a[i] <= b[j])) {
            std::cout << a[i];
            i++;
        } else {
            std::cout << b[j];
            j++;
        }
    }
    std::cout << "\n";
    return 0;
}
