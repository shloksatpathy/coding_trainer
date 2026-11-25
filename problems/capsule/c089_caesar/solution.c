#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    char line[1000];
    fgets(line, sizeof line, stdin);
    line[strcspn(line, "\n")] = '\0';
    int k;
    scanf("%d", &k);
    for (int i = 0; line[i] != '\0'; i++) {
        char ch = line[i];
        if (islower(ch)) {
            printf("%c", (ch - 'a' + k) % 26 + 'a');
        } else if (isupper(ch)) {
            printf("%c", (ch - 'A' + k) % 26 + 'A');
        } else {
            printf("%c", ch);
        }
    }
    printf("\n");
    return 0;
}
