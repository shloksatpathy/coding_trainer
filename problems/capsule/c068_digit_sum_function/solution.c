#include <stdio.h>

int digit_sum(int n) {
    int s = 0;
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

int main(void) {
    int n, x, best = -1, best_sum = -1;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (i > 0) {
            printf(" ");
        }
        printf("%d", digit_sum(x));
        if (digit_sum(x) > best_sum) {
            best_sum = digit_sum(x);
            best = x;
        }
    }
    printf("\nbest: %d\n", best);
    return 0;
}
