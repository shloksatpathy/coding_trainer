#include <iostream>
#include <string>

void back(const std::string &w, std::size_t i) {
    if (i == w.size()) {
        return;
    }
    back(w, i + 1);
    std::cout << w[i];
}

int main() {
    std::string w;
    std::cin >> w;
    back(w, 0);
    std::cout << "\n";
    return 0;
}
