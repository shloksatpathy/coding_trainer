#include <stdio.h>

int main(void) {
    int r, c;
    char g[100][101];
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) {
        scanf("%100s", g[i]);
    }
    for (int j = 0; j < c; j++) {
        for (int k = 0; k < r; k++) {
            printf("%c", g[r - 1 - k][j]);
        }
        printf("\n");
    }
    return 0;
}
