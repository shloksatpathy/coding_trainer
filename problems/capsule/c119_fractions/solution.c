#include <stdio.h>

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

struct Fraction add(struct Fraction f, struct Fraction g) {
    struct Fraction s = {f.num * g.den + g.num * f.den, f.den * g.den};
    int k = gcd(s.num, s.den);
    s.num /= k;
    s.den /= k;
    return s;
}

int main(void) {
    struct Fraction f, g;
    scanf("%d/%d %d/%d", &f.num, &f.den, &g.num, &g.den);
    struct Fraction s = add(f, g);
    printf("%d/%d\n", s.num, s.den);
    return 0;
}
