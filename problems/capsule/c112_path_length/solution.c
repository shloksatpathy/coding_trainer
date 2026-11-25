#include <math.h>
#include <stdio.h>

struct Point {
    int x;
    int y;
};

double distance(struct Point p, struct Point q) {
    double dx = q.x - p.x, dy = q.y - p.y;
    return sqrt(dx * dx + dy * dy);
}

int main(void) {
    int n;
    struct Point pts[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &pts[i].x, &pts[i].y);
    }
    double total = 0;
    for (int i = 1; i < n; i++) {
        total += distance(pts[i - 1], pts[i]);
    }
    printf("%.2f\n", total);
    return 0;
}
