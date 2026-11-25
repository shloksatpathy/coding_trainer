#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int first = a[0];
    for (int i = 0; i < n; i++) {
        if (a[i] > first) {
            first = a[i];
        }
    }
    bool found = false;
    int second = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] < first && (!found || a[i] > second)) {
            second = a[i];
            found = true;
        }
    }
    if (found) {
        std::cout << second << "\n";
    } else {
        std::cout << "none\n";
    }
    return 0;
}
