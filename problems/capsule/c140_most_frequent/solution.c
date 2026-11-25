#include <stdio.h>
#include <stdlib.h>

long long a[200000];

int compare(const void *p, const void *q) {
    long long x = *(const long long *)p, y = *(const long long *)q;
    return (x > y) - (x < y);
}

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
    }
    qsort(a, n, sizeof a[0], compare);
    long long best = a[0];
    int best_count = 0, distinct = 0;
    for (int i = 0; i < n;) {
        int j = i;
        while (j < n && a[j] == a[i]) {
            j++;
        }
        distinct++;
        if (j - i > best_count) {
            best_count = j - i;
            best = a[i];
        }
        i = j;
    }
    printf("value: %lld\n", best);
    printf("count: %d\n", best_count);
    printf("distinct: %d\n", distinct);
    return 0;
}
