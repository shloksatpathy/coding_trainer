#include <stdio.h>

int main(void) {
    int n;
    int a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int x, count = 0;
    scanf("%d", &x);
    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            count++;
        }
    }
    printf("count: %d\n", count);
    printf("positions:");
    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            printf(" %d", i + 1);
        }
    }
    if (count == 0) {
        printf(" none");
    }
    printf("\n");
    return 0;
}
