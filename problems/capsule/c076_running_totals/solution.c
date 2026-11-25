#include <stdio.h>

int main(void) {
    int n;
    int a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += a[i];
        if (i > 0) {
            printf(" ");
        }
        printf("%d", total);
    }
    printf("\n");
    return 0;
}
