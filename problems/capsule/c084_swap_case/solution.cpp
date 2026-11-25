#include <cctype>
#include <iostream>
#include <string>

int main() {
    std::string line;
    std::getline(std::cin, line);
    for (std::size_t i = 0; i < line.size(); i++) {
        char ch = line[i];
        if (std::isupper(ch)) {
            std::cout << (char)std::tolower(ch);
        } else if (std::islower(ch)) {
            std::cout << (char)std::toupper(ch);
        } else {
            std::cout << ch;
        }
    }
    std::cout << "\n";
    return 0;
}
