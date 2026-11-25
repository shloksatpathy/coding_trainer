#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    printf("last digit: %d\n", n % 10);
    printf("without it: %d\n", n / 10);
    return 0;
}
