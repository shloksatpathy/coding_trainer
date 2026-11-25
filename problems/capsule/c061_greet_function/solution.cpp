#include <iostream>
#include <string>

void greet(std::string name) {
    std::cout << "Hello, " << name << "!\n";
}

int main() {
    std::string name;
    for (int i = 0; i < 3; i++) {
        std::cin >> name;
        greet(name);
    }
    return 0;
}
