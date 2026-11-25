#include <stdio.h>
#include <string.h>

int main(void) {
    char line[1000];
    fgets(line, sizeof line, stdin);
    line[strcspn(line, "\n")] = '\0';
    for (int i = strlen(line) - 1; i >= 0; i--) {
        printf("%c", line[i]);
    }
    printf("\n");
    return 0;
}
