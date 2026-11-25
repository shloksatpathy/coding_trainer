#include <stdio.h>

int main(void) {
    int total, count;
    scanf("%d %d", &total, &count);
    printf("whole: %d\n", total / count);
    printf("exact: %.3f\n", (double)total / count);
    return 0;
}
