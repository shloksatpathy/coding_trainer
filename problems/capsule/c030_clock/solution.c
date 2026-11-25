#include <stdio.h>

int main(void) {
    int s;
    scanf("%d", &s);
    printf("%d:%02d:%02d\n", s / 3600, s / 60 % 60, s % 60);
    return 0;
}
