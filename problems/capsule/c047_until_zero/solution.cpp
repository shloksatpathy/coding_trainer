#include <iostream>

int main() {
    int x, count = 0, total = 0;
    while (true) {
        std::cin >> x;
        if (x == 0) {
            break;
        }
        count++;
        total += x;
    }
    std::cout << "count: " << count << "\n";
    std::cout << "sum: " << total << "\n";
    return 0;
}
