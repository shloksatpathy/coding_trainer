#include <cctype>
#include <iostream>
#include <string>

int main() {
    std::string line;
    std::getline(std::cin, line);
    int count = 0;
    for (std::size_t i = 0; i < line.size(); i++) {
        char ch = std::tolower(line[i]);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            count++;
        }
    }
    std::cout << count << "\n";
    return 0;
}
