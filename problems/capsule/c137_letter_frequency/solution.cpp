#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string line;
    std::getline(std::cin, line);
    std::vector<int> count(26, 0);
    for (std::size_t i = 0; i < line.size(); i++) {
        if (std::isalpha(line[i])) {
            count[std::tolower(line[i]) - 'a']++;
        }
    }
    std::vector<int> order;
    for (int i = 0; i < 26; i++) {
        if (count[i] > 0) {
            order.push_back(i);
        }
    }
    std::sort(order.begin(), order.end(), [&](int x, int y) {
        if (count[x] != count[y]) {
            return count[x] > count[y];
        }
        return x < y;
    });
    for (std::size_t i = 0; i < order.size(); i++) {
        std::cout << (char)('a' + order[i]) << ": " << count[order[i]] << "\n";
    }
    return 0;
}
