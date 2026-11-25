#include <stdio.h>

int main(void) {
    long long total = 0, term, x;
    char op[2];
    scanf("%lld", &term);
    while (scanf("%1s %lld", op, &x) == 2) {
        if (op[0] == '*') {
            term *= x;
        } else {
            total += term;
            if (op[0] == '+') {
                term = x;
            } else {
                term = -x;
            }
        }
    }
    printf("%lld\n", total + term);
    return 0;
}
