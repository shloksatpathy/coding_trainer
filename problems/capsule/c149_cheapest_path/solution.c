#include <stdio.h>

int g[100][100];
long long best[100][100];

int main(void) {
    int r, c;
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &g[i][j]);
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (i == 0 && j == 0) {
                best[i][j] = g[i][j];
            } else if (i == 0) {
                best[i][j] = best[i][j - 1] + g[i][j];
            } else if (j == 0) {
                best[i][j] = best[i - 1][j] + g[i][j];
            } else if (best[i - 1][j] < best[i][j - 1]) {
                best[i][j] = best[i - 1][j] + g[i][j];
            } else {
                best[i][j] = best[i][j - 1] + g[i][j];
            }
        }
    }
    printf("%lld\n", best[r - 1][c - 1]);
    return 0;
}
