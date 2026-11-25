#include <stdio.h>

long long a[200000];

#define SIZE 524288

long long keys[SIZE];
int used[SIZE];
int vals[SIZE];

int slot(long long key) {
    unsigned long long h = (unsigned long long)key * 11400714819323198485ull;
    int i = h >> 45;
    while (used[i] && keys[i] != key) {
        i = (i + 1) & (SIZE - 1);
    }
    return i;
}

int main(void) {
    int n;
    long long t;
    scanf("%d %lld", &n, &t);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
    }
    for (int j = 0; j < n; j++) {
        int k = slot(t - a[j]);
        if (used[k]) {
            printf("%d %d\n", vals[k] + 1, j + 1);
            return 0;
        }
        k = slot(a[j]);
        if (!used[k]) {
            used[k] = 1;
            keys[k] = a[j];
            vals[k] = j;
        }
    }
    printf("none\n");
    return 0;
}
