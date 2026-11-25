#include <stdio.h>

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    int q = a / b;
    int r = a % b;
    printf("a / b = %d\n", q);
    printf("a %% b = %d\n", r);
    printf("Q * b + R = %d\n", q * b + r);
    return 0;
}
