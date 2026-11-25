#include <stdio.h>

void greet(char name[]) {
    printf("Hello, %s!\n", name);
}

int main(void) {
    char name[100];
    for (int i = 0; i < 3; i++) {
        scanf("%99s", name);
        greet(name);
    }
    return 0;
}
