#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    char line[1000];
    fgets(line, sizeof line, stdin);
    line[strcspn(line, "\n")] = '\0';
    for (int i = 0; line[i] != '\0'; i++) {
        if (isupper(line[i])) {
            printf("%c", tolower(line[i]));
        } else if (islower(line[i])) {
            printf("%c", toupper(line[i]));
        } else {
            printf("%c", line[i]);
        }
    }
    printf("\n");
    return 0;
}
