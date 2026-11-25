#include <stdio.h>

int main(void) {
    int x, count = 0, total = 0;
    while (1) {
        scanf("%d", &x);
        if (x == 0) {
            break;
        }
        count++;
        total += x;
    }
    printf("count: %d\n", count);
    printf("sum: %d\n", total);
    return 0;
}
