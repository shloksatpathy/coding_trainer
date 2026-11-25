#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    int n, q;
    std::cin >> n;
    std::unordered_map<std::string, std::string> book;
    std::string name, number;
    for (int i = 0; i < n; i++) {
        std::cin >> name >> number;
        book[name] = number;
    }
    std::cin >> q;
    for (int i = 0; i < q; i++) {
        std::cin >> name;
        if (book.count(name)) {
            std::cout << name << ": " << book[name] << "\n";
        } else {
            std::cout << name << ": not found\n";
        }
    }
    return 0;
}
