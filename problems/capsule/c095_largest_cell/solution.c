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
    int best = g[0][0], br = 0, bc = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (g[i][j] > best) {
                best = g[i][j];
                br = i;
                bc = j;
            }
        }
    }
    printf("max: %d at %d %d\n", best, br + 1, bc + 1);
    return 0;
}
