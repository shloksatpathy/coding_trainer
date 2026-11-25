#include <stdio.h>

long long power(long long base, int exp) {
    long long result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main(void) {
    long long base;
    int exp;
    scanf("%lld %d", &base, &exp);
    printf("%lld\n", power(base, exp));
    return 0;
}
