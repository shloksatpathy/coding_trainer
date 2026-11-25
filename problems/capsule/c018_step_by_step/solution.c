#include <stdio.h>

int main(void) {
    int x;
    scanf("%d", &x);
    printf("start: %d\n", x);
    x += 5;
    printf("+5: %d\n", x);
    x *= 2;
    printf("*2: %d\n", x);
    x -= 3;
    printf("-3: %d\n", x);
    return 0;
}
