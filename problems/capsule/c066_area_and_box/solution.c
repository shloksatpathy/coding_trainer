#include <stdio.h>

int area(int w, int h) {
    return w * h;
}

void draw_box(int w, int h) {
    for (int r = 0; r < h; r++) {
        for (int col = 0; col < w; col++) {
            printf("*");
        }
        printf("\n");
    }
}

int main(void) {
    int w, h;
    scanf("%d %d", &w, &h);
    printf("area: %d\n", area(w, h));
    draw_box(w, h);
    return 0;
}
