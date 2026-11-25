#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << "before: a=" << a << " b=" << b << "\n";
    int t = a;
    a = b;
    b = t;
    std::cout << "after: a=" << a << " b=" << b << "\n";
    return 0;
}
