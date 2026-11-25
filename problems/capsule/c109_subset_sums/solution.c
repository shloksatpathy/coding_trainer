#include <stdio.h>

int n;
int a[20];

int count(int i, int left) {
    if (i == n) {
        if (left == 0) {
            return 1;
        }
        return 0;
    }
    return count(i + 1, left) + count(i + 1, left - a[i]);
}

int main(void) {
    int t;
    scanf("%d %d", &n, &t);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    printf("%d\n", count(0, t));
    return 0;
}
