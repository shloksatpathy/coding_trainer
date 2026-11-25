#include <stdio.h>

int a[200000];

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int q, x;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        scanf("%d", &x);
        int lo = 0, hi = n - 1, pos = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] == x) {
                pos = mid + 1;
                break;
            }
            if (a[mid] < x) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        printf("%d\n", pos);
    }
    return 0;
}
