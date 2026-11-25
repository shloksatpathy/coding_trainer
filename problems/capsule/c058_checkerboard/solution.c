#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for (int r = 0; r < n; r++) {
        for (int col = 0; col < n; col++) {
            if ((r + col) % 2 == 0) {
                printf("#");
            } else {
                printf(".");
            }
        }
        printf("\n");
    }
    return 0;
}
