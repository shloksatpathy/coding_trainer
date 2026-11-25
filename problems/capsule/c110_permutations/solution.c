#include <stdbool.h>
#include <stdio.h>

int cur[6];
bool used[7];

void perm(int pos, int n) {
    if (pos == n) {
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                printf(" ");
            }
            printf("%d", cur[i]);
        }
        printf("\n");
        return;
    }
    for (int x = 1; x <= n; x++) {
        if (!used[x]) {
            used[x] = true;
            cur[pos] = x;
            perm(pos + 1, n);
            used[x] = false;
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    perm(0, n);
    return 0;
}
