#include <stdio.h>

int a[200000];

int main(void) {
    int n, t;
    scanf("%d %d", &n, &t);
    for (int k = 0; k < n; k++) {
        scanf("%d", &a[k]);
    }
    int i = 0, j = n - 1, found = 0;
    while (i < j) {
        int s = a[i] + a[j];
        if (s == t) {
            printf("%d %d\n", a[i], a[j]);
            found++;
            i++;
            j--;
        } else if (s < t) {
            i++;
        } else {
            j--;
        }
    }
    if (found == 0) {
        printf("none\n");
    }
    return 0;
}
