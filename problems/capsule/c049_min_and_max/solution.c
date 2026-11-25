#include <stdio.h>

int main(void) {
    int n, x;
    scanf("%d %d", &n, &x);
    int lo = x, hi = x;
    for (int i = 1; i < n; i++) {
        scanf("%d", &x);
        if (x < lo) {
            lo = x;
        }
        if (x > hi) {
            hi = x;
        }
    }
    printf("min: %d\n", lo);
    printf("max: %d\n", hi);
    return 0;
}
