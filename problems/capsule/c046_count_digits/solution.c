#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int digits = 1;
    while (n >= 10) {
        n /= 10;
        digits++;
    }
    printf("%d\n", digits);
    return 0;
}
