#include <stdio.h>

int main(void) {
    int n;
    int g[100][100];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &g[i][j]);
        }
    }
    int main_sum = 0, anti = 0;
    for (int i = 0; i < n; i++) {
        main_sum += g[i][i];
        anti += g[i][n - 1 - i];
    }
    printf("main: %d\n", main_sum);
    printf("anti: %d\n", anti);
    return 0;
}
