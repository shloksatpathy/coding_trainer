#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int k = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", k);
            k++;
        }
        printf("\n");
    }
    return 0;
}
