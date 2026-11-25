#include <stdio.h>

int main(void) {
    int n;
    int a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int total = 0, found = 0;
    for (int i = 0; i < n; i++) {
        total += a[i];
    }
    printf("average: %.2f\n", (double)total / n);
    for (int i = 0; i < n; i++) {
        if (a[i] * n > total) {
            if (found > 0) {
                printf(" ");
            }
            printf("%d", a[i]);
            found++;
        }
    }
    if (found == 0) {
        printf("none\n");
    } else {
        printf("\n");
    }
    return 0;
}
