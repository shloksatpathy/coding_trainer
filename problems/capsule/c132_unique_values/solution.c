#include <stdio.h>

long long a[1000], out[1000];

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
    }
    int k = 0;
    for (int i = 0; i < n; i++) {
        int seen = 0;
        for (int j = 0; j < k; j++) {
            if (out[j] == a[i]) {
                seen = 1;
            }
        }
        if (!seen) {
            out[k] = a[i];
            k++;
        }
    }
    for (int i = 0; i < k; i++) {
        if (i > 0) {
            printf(" ");
        }
        printf("%lld", out[i]);
    }
    printf("\ndistinct: %d\n", k);
    return 0;
}
