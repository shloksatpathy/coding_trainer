#include <stdio.h>

long long a[200000];

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
    }
    long long here = a[0], best = a[0];
    for (int i = 1; i < n; i++) {
        if (here > 0) {
            here += a[i];
        } else {
            here = a[i];
        }
        if (here > best) {
            best = here;
        }
    }
    printf("%lld\n", best);
    return 0;
}
