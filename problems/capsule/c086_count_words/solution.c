#include <stdio.h>

int main(void) {
    char w[100];
    int count = 0;
    while (scanf("%99s", w) == 1) {
        count++;
    }
    printf("%d\n", count);
    return 0;
}
