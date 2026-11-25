#include <stdio.h>

int a[100000], b[100000];

int main(void) {
    int n, m;
    scanf("%d", &n);
    for (int k = 0; k < n; k++) {
        scanf("%d", &a[k]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &b[k]);
    }
    int i = 0, j = 0;
    for (int k = 0; k < n + m; k++) {
        if (k > 0) {
            printf(" ");
        }
        if (j == m || (i < n && a[i] <= b[j])) {
            printf("%d", a[i]);
            i++;
        } else {
            printf("%d", b[j]);
            j++;
        }
    }
    printf("\n");
    return 0;
}
