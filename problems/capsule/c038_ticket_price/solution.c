#include <stdio.h>

int main(void) {
    int age;
    scanf("%d", &age);
    if (age < 3) {
        printf("free\n");
    } else if (age < 13) {
        printf("child 5\n");
    } else if (age < 65) {
        printf("adult 12\n");
    } else {
        printf("senior 7\n");
    }
    return 0;
}
