#include <stdio.h>

int main(void) {
    char name[100], city[100];
    int year;
    scanf("%99s %99s %d", name, city, &year);
    printf("%s from %s, since %d\n", name, city, year);
    printf("That is %d years before 2026.\n", 2026 - year);
    return 0;
}
