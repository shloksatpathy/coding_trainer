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
        int pos = -1;
        for (int i = 0; i < n; i++) {
            if (a[i] == x) {
                pos = i + 1;
                break;
            }
        }
        printf("%d\n", pos);
    }
    return 0;
}
