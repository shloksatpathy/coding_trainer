#include <stdio.h>
#include <string.h>

int main(void) {
    char line[200];
    fgets(line, sizeof line, stdin);
    line[strcspn(line, "\n")] = '\0';
    printf("You said: %s\n", line);
    return 0;
}
