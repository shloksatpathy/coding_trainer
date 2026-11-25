#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for (int r = 1; r <= n; r++) {
        for (int col = 1; col <= n; col++) {
            printf("%4d", r * col);
        }
        printf("\n");
    }
    return 0;
}
