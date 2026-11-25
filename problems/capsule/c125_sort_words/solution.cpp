#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

bool before(const std::string &a, const std::string &b) {
    if (a.size() != b.size()) {
        return a.size() < b.size();
    }
    return a < b;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> words(n);
    for (int i = 0; i < n; i++) {
        std::cin >> words[i];
    }
    std::sort(words.begin(), words.end(), before);
    for (int i = 0; i < n; i++) {
        std::cout << words[i] << "\n";
    }
    return 0;
}
