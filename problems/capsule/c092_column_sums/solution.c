#include <stdio.h>

int main(void) {
    int r, c;
    int g[100][100];
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &g[i][j]);
        }
    }
    for (int j = 0; j < c; j++) {
        int total = 0;
        for (int i = 0; i < r; i++) {
            total += g[i][j];
        }
        if (j > 0) {
            printf(" ");
        }
        printf("%d", total);
    }
    printf("\n");
    return 0;
}
