#include <stdio.h>

int main(void) {
    char w[100];
    int count = 0;
    while (scanf("%99s", w) == 1) {
        if (count > 0) {
            printf("-");
        }
        printf("%s", w);
        count++;
    }
    printf("\n");
    return 0;
}
