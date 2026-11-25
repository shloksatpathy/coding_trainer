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
        for (int i = 0; i < r; i++) {
            if (i > 0) {
                printf(" ");
            }
            printf("%d", g[i][j]);
        }
        printf("\n");
    }
    return 0;
}
