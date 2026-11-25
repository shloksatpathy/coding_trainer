#include <iostream>

int main() {
    int age;
    std::cin >> age;
    if (age < 3) {
        std::cout << "free\n";
    } else if (age < 13) {
        std::cout << "child 5\n";
    } else if (age < 65) {
        std::cout << "adult 12\n";
    } else {
        std::cout << "senior 7\n";
    }
    return 0;
}
