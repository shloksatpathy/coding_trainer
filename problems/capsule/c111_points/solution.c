#include <stdio.h>
#include <stdlib.h>

struct Point {
    int x;
    int y;
};

int main(void) {
    struct Point p, q;
    scanf("%d %d %d %d", &p.x, &p.y, &q.x, &q.y);
    int dx = q.x - p.x, dy = q.y - p.y;
    printf("dx: %d\n", dx);
    printf("dy: %d\n", dy);
    printf("manhattan: %d\n", abs(dx) + abs(dy));
    return 0;
}
