#include <stdio.h>

int main(void) {
    const int THIS_YEAR = 2026;
    char name[100];
    int age;
    scanf("%99s %d", name, &age);
    int born = THIS_YEAR - age;
    printf("Hello, %s! You are %d.\n", name, age);
    printf("In 10 years you will be %d.\n", age + 10);
    printf("You were born in %d or %d.\n", born, born - 1);
    return 0;
}
