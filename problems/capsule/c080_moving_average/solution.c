#include <stdio.h>

int main(void) {
    int n, k;
    int a[1000];
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int window = 0;
    for (int i = 0; i < k; i++) {
        window += a[i];
    }
    printf("%.2f", (double)window / k);
    for (int i = k; i < n; i++) {
        window += a[i] - a[i - k];
        printf(" %.2f", (double)window / k);
    }
    printf("\n");
    return 0;
}
