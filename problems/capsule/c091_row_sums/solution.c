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
    for (int i = 0; i < r; i++) {
        int total = 0;
        for (int j = 0; j < c; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", g[i][j]);
            total += g[i][j];
        }
        printf(" | %d\n", total);
    }
    return 0;
}
