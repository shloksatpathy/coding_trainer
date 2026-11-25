#include <stdio.h>

int absolute(int x) {
    if (x < 0) {
        return -x;
    }
    return x;
}

int distance(int a, int b) {
    return absolute(a - b);
}

int main(void) {
    int n, a, b;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", distance(a, b));
    }
    return 0;
}
