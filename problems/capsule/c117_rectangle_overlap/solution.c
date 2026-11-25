#include <stdio.h>

struct Rect {
    int x1, y1, x2, y2;
};

int min(int a, int b) {
    if (a < b) {
        return a;
    }
    return b;
}

int max(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int overlap_area(struct Rect a, struct Rect b) {
    int w = min(a.x2, b.x2) - max(a.x1, b.x1);
    int h = min(a.y2, b.y2) - max(a.y1, b.y1);
    if (w <= 0 || h <= 0) {
        return 0;
    }
    return w * h;
}

int main(void) {
    struct Rect a, b;
    scanf("%d %d %d %d", &a.x1, &a.y1, &a.x2, &a.y2);
    scanf("%d %d %d %d", &b.x1, &b.y1, &b.x2, &b.y2);
    printf("%d\n", overlap_area(a, b));
    return 0;
}
