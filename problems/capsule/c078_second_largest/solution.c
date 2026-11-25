#include <stdio.h>

int main(void) {
    int n;
    int a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int first = a[0];
    for (int i = 0; i < n; i++) {
        if (a[i] > first) {
            first = a[i];
        }
    }
    int found = 0, second = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] < first && (!found || a[i] > second)) {
            second = a[i];
            found = 1;
        }
    }
    if (found) {
        printf("%d\n", second);
    } else {
        printf("none\n");
    }
    return 0;
}
