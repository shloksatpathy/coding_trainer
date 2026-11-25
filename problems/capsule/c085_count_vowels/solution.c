#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    char line[1000];
    fgets(line, sizeof line, stdin);
    line[strcspn(line, "\n")] = '\0';
    int count = 0;
    for (int i = 0; line[i] != '\0'; i++) {
        char ch = tolower(line[i]);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}
