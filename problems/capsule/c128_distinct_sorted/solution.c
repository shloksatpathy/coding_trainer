#include <stdio.h>

int a[200000];

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int k = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || a[i] != a[i - 1]) {
            if (k > 0) {
                printf(" ");
            }
            printf("%d", a[i]);
            k++;
        }
    }
    printf("\ndistinct: %d\n", k);
    return 0;
}
