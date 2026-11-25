#include <iostream>
#include <string>

int main() {
    const int THIS_YEAR = 2026;
    std::string name;
    int age;
    std::cin >> name >> age;
    int born = THIS_YEAR - age;
    std::cout << "Hello, " << name << "! You are " << age << ".\n";
    std::cout << "In 10 years you will be " << age + 10 << ".\n";
    std::cout << "You were born in " << born << " or " << born - 1 << ".\n";
    return 0;
}
