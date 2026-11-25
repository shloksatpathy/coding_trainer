#include <stdio.h>

int main(void) {
    int n;
    int a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int count[10] = {0};
    for (int i = 0; i < n; i++) {
        count[a[i]]++;
    }
    for (int v = 0; v < 10; v++) {
        if (count[v] > 0) {
            printf("%d: %d\n", v, count[v]);
        }
    }
    return 0;
}
