#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::vector<int> count(10, 0);
    for (int i = 0; i < n; i++) {
        count[a[i]]++;
    }
    for (int v = 0; v < 10; v++) {
        if (count[v] > 0) {
            std::cout << v << ": " << count[v] << "\n";
        }
    }
    return 0;
}
