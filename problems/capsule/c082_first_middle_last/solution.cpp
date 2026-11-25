#include <iostream>
#include <string>

int main() {
    std::string w;
    std::cin >> w;
    int n = w.size();
    std::cout << "first: " << w[0] << "\n";
    std::cout << "middle: " << w[n / 2] << "\n";
    std::cout << "last: " << w[n - 1] << "\n";
    return 0;
}
