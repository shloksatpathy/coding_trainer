#include <stdio.h>

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("before: a=%d b=%d\n", a, b);
    int t = a;
    a = b;
    b = t;
    printf("after: a=%d b=%d\n", a, b);
    return 0;
}
