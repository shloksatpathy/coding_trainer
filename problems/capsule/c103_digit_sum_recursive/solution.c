#include <stdio.h>

int digit_sum(int n) {
    if (n < 10) {
        return n;
    }
    return n % 10 + digit_sum(n / 10);
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\n", digit_sum(n));
    return 0;
}
