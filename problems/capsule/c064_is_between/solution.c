#include <stdbool.h>
#include <stdio.h>

bool is_between(int x, int lo, int hi) {
    return lo <= x && x <= hi;
}

int main(void) {
    int lo, hi, n, x;
    scanf("%d %d %d", &lo, &hi, &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (is_between(x, lo, hi)) {
            printf("yes\n");
        } else {
            printf("no\n");
        }
    }
    return 0;
}
