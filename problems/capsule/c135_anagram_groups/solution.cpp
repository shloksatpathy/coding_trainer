#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::unordered_map<std::string, int> group;
    std::vector<std::vector<std::string>> groups;
    std::string w;
    for (int i = 0; i < n; i++) {
        std::cin >> w;
        std::string key = w;
        std::sort(key.begin(), key.end());
        if (group.count(key) == 0) {
            group[key] = groups.size();
            groups.push_back({});
        }
        groups[group[key]].push_back(w);
    }
    for (std::size_t g = 0; g < groups.size(); g++) {
        for (std::size_t i = 0; i < groups[g].size(); i++) {
            if (i > 0) {
                std::cout << " ";
            }
            std::cout << groups[g][i];
        }
        std::cout << "\n";
    }
    return 0;
}
