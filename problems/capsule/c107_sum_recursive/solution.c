#include <stdio.h>

int total(int a[], int i, int n) {
    if (i == n) {
        return 0;
    }
    return a[i] + total(a, i + 1, n);
}

int main(void) {
    int n;
    int a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    printf("%d\n", total(a, 0, n));
    return 0;
}
