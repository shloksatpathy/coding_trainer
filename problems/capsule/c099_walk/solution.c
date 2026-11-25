#include <stdio.h>

int main(void) {
    int r, c;
    char g[100][101];
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) {
        scanf("%100s", g[i]);
    }
    char moves[1001];
    scanf("%1000s", moves);
    int row = 0, col = 0, moved = 0;
    for (int i = 0; moves[i] != '\0'; i++) {
        int nr = row, nc = col;
        if (moves[i] == 'U') {
            nr--;
        } else if (moves[i] == 'D') {
            nr++;
        } else if (moves[i] == 'L') {
            nc--;
        } else {
            nc++;
        }
        if (nr >= 0 && nr < r && nc >= 0 && nc < c && g[nr][nc] == '.') {
            row = nr;
            col = nc;
            moved++;
        }
    }
    printf("at %d %d\n", row + 1, col + 1);
    printf("moved: %d\n", moved);
    return 0;
}
