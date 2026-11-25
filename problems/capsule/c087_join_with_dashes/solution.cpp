#include <iostream>
#include <string>

int main() {
    std::string w;
    int count = 0;
    while (std::cin >> w) {
        if (count > 0) {
            std::cout << "-";
        }
        std::cout << w;
        count++;
    }
    std::cout << "\n";
    return 0;
}
