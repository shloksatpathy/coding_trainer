#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int first = 1;
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0) {
            continue;
        }
        if (!first) {
            printf(" ");
        }
        printf("%d", i);
        first = 0;
    }
    printf("\n");
    return 0;
}
