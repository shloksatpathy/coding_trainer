#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int x, count = 0;
    std::cin >> x;
    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            count++;
        }
    }
    std::cout << "count: " << count << "\n";
    std::cout << "positions:";
    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            std::cout << " " << i + 1;
        }
    }
    if (count == 0) {
        std::cout << " none";
    }
    std::cout << "\n";
    return 0;
}
