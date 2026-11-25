#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for (int r = 0; r < n; r++) {
        for (int col = 0; col < n; col++) {
            if (r == 0 || r == n - 1 || col == 0 || col == n - 1) {
                printf("#");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}
