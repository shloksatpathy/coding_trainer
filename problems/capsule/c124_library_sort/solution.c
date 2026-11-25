#include <stdio.h>
#include <stdlib.h>

int a[200000];

int compare(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    if (x < y) {
        return -1;
    }
    if (x > y) {
        return 1;
    }
    return 0;
}

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    qsort(a, n, sizeof a[0], compare);
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            printf(" ");
        }
        printf("%d", a[i]);
    }
    printf("\n");
    for (int i = n - 1; i >= 0; i--) {
        if (i < n - 1) {
            printf(" ");
        }
        printf("%d", a[i]);
    }
    printf("\n");
    return 0;
}
