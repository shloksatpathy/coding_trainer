#include <iostream>
#include <string>
#include <vector>

struct Item {
    std::string id;
    int qty;
};

int find(const std::vector<Item> &items, const std::string &key) {
    for (std::size_t i = 0; i < items.size(); i++) {
        if (items[i].id == key) {
            return i;
        }
    }
    return -1;
}

int main() {
    int n, m, change;
    std::string key;
    std::cin >> n;
    std::vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        std::cin >> items[i].id >> items[i].qty;
    }
    std::cin >> m;
    for (int i = 0; i < m; i++) {
        std::cin >> key >> change;
        int k = find(items, key);
        if (k == -1) {
            std::cout << "unknown " << key << "\n";
        } else {
            items[k].qty += change;
        }
    }
    for (int i = 0; i < n; i++) {
        std::cout << items[i].id << ": " << items[i].qty << "\n";
    }
    return 0;
}
