#include <stdio.h>

int main(void) {
    int secret, n, g;
    scanf("%d %d", &secret, &n);
    int found = 0;
    for (int k = 1; k <= n; k++) {
        scanf("%d", &g);
        if (g < secret) {
            printf("too low\n");
        } else if (g > secret) {
            printf("too high\n");
        } else {
            printf("correct on guess %d\n", k);
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("no luck, it was %d\n", secret);
    }
    return 0;
}
