#include <iostream>

struct Fraction {
    int num, den;
};

int gcd(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

Fraction add(Fraction f, Fraction g) {
    Fraction s = {f.num * g.den + g.num * f.den, f.den * g.den};
    int k = gcd(s.num, s.den);
    s.num /= k;
    s.den /= k;
    return s;
}

int main() {
    Fraction f, g;
    char slash;
    std::cin >> f.num >> slash >> f.den >> g.num >> slash >> g.den;
    Fraction s = add(f, g);
    std::cout << s.num << "/" << s.den << "\n";
    return 0;
}
