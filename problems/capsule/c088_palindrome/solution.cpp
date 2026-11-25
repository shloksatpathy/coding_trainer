#include <iostream>
#include <string>

int main() {
    std::string w;
    std::cin >> w;
    int i = 0, j = w.size() - 1;
    bool same = true;
    while (i < j) {
        if (w[i] != w[j]) {
            same = false;
            break;
        }
        i++;
        j--;
    }
    if (same) {
        std::cout << "yes\n";
    } else {
        std::cout << "no\n";
    }
    return 0;
}
