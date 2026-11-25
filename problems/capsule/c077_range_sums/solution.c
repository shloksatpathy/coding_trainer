#include <stdio.h>

int main(void) {
    int n;
    int a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int p[1001];
    p[0] = 0;
    for (int i = 1; i <= n; i++) {
        p[i] = p[i - 1] + a[i - 1];
    }
    int q, l, r;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        scanf("%d %d", &l, &r);
        printf("%d\n", p[r] - p[l - 1]);
    }
    return 0;
}
