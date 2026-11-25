#include <stdio.h>

struct Time {
    int h, m;
};

int to_minutes(struct Time t) {
    return t.h * 60 + t.m;
}

int main(void) {
    struct Time a, b;
    scanf("%d:%d %d:%d", &a.h, &a.m, &b.h, &b.m);
    int d = to_minutes(b) - to_minutes(a);
    printf("%d:%02d\n", d / 60, d % 60);
    return 0;
}
