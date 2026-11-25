#include <stdbool.h>
#include <stdio.h>

char g[3][4];

bool wins(char p) {
    for (int i = 0; i < 3; i++) {
        if (g[i][0] == p && g[i][1] == p && g[i][2] == p) {
            return true;
        }
        if (g[0][i] == p && g[1][i] == p && g[2][i] == p) {
            return true;
        }
    }
    if (g[0][0] == p && g[1][1] == p && g[2][2] == p) {
        return true;
    }
    return g[0][2] == p && g[1][1] == p && g[2][0] == p;
}

int main(void) {
    for (int i = 0; i < 3; i++) {
        scanf("%3s", g[i]);
    }
    int full = 1;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (g[i][j] == '.') {
                full = 0;
            }
        }
    }
    if (wins('X')) {
        printf("X wins\n");
    } else if (wins('O')) {
        printf("O wins\n");
    } else if (full) {
        printf("draw\n");
    } else {
        printf("in progress\n");
    }
    return 0;
}
