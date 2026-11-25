#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for (int k = 1; k <= 2 * n - 1; k++) {
        int i;
        if (k <= n) {
            i = k;
        } else {
            i = 2 * n - k;
        }
        for (int j = 0; j < n - i; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
