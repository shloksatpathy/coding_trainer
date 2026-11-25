#include <stdio.h>

int main(void) {
    int r, c;
    char g[100][101];
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) {
        scanf("%100s", g[i]);
    }
    int total = 0;
    for (int i = 0; i < r; i++) {
        int count = 0;
        for (int j = 0; j < c; j++) {
            if (g[i][j] == '#') {
                count++;
            }
        }
        printf("%d\n", count);
        total += count;
    }
    printf("total: %d\n", total);
    return 0;
}
