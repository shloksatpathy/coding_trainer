#include <stdio.h>

int main(void) {
    int r, c;
    char g[100][101];
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) {
        scanf("%100s", g[i]);
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (g[i][j] == '*') {
                printf("*");
                continue;
            }
            int count = 0;
            for (int di = -1; di <= 1; di++) {
                for (int dj = -1; dj <= 1; dj++) {
                    int ni = i + di, nj = j + dj;
                    if (ni >= 0 && ni < r && nj >= 0 && nj < c && g[ni][nj] == '*') {
                        count++;
                    }
                }
            }
            printf("%d", count);
        }
        printf("\n");
    }
    return 0;
}
