#include <stdio.h>

int main(void) {
    int d;
    scanf("%d", &d);
    if (d == 6 || d == 7) {
        printf("weekend\n");
    } else if (d >= 1 && d <= 5) {
        printf("weekday\n");
    } else {
        printf("invalid\n");
    }
    return 0;
}
