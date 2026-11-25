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
    long long best = (long long)a[1] - a[0];
    for (int i = 2; i < n; i++) {
        if ((long long)a[i] - a[i - 1] < best) {
            best = (long long)a[i] - a[i - 1];
        }
    }
    printf("%lld\n", best);
    return 0;
}
