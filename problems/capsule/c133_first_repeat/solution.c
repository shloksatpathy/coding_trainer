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
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
    }
    for (int i = 0; i < n; i++) {
        int k = slot(a[i]);
        if (used[k]) {
            printf("%lld\n", a[i]);
            return 0;
        }
        used[k] = 1;
        keys[k] = a[i];
    }
    printf("none\n");
    return 0;
}
