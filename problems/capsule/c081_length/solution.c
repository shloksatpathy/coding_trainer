#include <stdio.h>
#include <string.h>

int main(void) {
    char line[1000];
    fgets(line, sizeof line, stdin);
    line[strcspn(line, "\n")] = '\0';
    printf("%zu\n", strlen(line));
    return 0;
}
