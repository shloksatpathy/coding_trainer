#include <stdio.h>

int square(int x) {
    return x * x;
}

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", square(a) + square(b));
    return 0;
}
