#include <stdio.h>
#include <string.h>

int main(void) {
    char w[100];
    scanf("%99s", w);
    int n = strlen(w);
    printf("first: %c\n", w[0]);
    printf("middle: %c\n", w[n / 2]);
    printf("last: %c\n", w[n - 1]);
    return 0;
}
