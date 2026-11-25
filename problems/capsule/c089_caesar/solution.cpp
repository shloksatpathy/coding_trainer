#include <cctype>
#include <iostream>
#include <string>

int main() {
    std::string line;
    std::getline(std::cin, line);
    int k;
    std::cin >> k;
    for (std::size_t i = 0; i < line.size(); i++) {
        char ch = line[i];
        if (std::islower(ch)) {
            std::cout << (char)((ch - 'a' + k) % 26 + 'a');
        } else if (std::isupper(ch)) {
            std::cout << (char)((ch - 'A' + k) % 26 + 'A');
        } else {
            std::cout << ch;
        }
    }
    std::cout << "\n";
    return 0;
}
