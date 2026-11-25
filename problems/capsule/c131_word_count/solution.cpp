#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::unordered_map<std::string, int> count;
    std::vector<std::string> order;
    std::string w;
    for (int i = 0; i < n; i++) {
        std::cin >> w;
        if (count.count(w) == 0) {
            order.push_back(w);
        }
        count[w]++;
    }
    for (std::size_t i = 0; i < order.size(); i++) {
        std::cout << order[i] << ": " << count[order[i]] << "\n";
    }
    return 0;
}
