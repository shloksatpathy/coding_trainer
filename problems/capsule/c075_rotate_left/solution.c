#include <stdio.h>

int main(void) {
    int n;
    int a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int k;
    scanf("%d", &k);
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            printf(" ");
        }
        printf("%d", a[(i + k) % n]);
    }
    printf("\n");
    return 0;
}
