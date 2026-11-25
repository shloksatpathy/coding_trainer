#include <iostream>
#include <string>

int main() {
    std::string line;
    std::getline(std::cin, line);
    for (int i = line.size() - 1; i >= 0; i--) {
        std::cout << line[i];
    }
    std::cout << "\n";
    return 0;
}
