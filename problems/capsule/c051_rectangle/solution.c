#include <stdio.h>

int main(void) {
    int w, h;
    scanf("%d %d", &w, &h);
    for (int r = 0; r < h; r++) {
        for (int col = 0; col < w; col++) {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
