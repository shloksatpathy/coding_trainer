#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    if (n >= 1 && n <= 100) {
        printf("inside\n");
    } else {
        printf("outside\n");
    }
    return 0;
}
