#include <stdio.h>
#include <string.h>

char words[1000][100];

int main(void) {
    int n, top = 0;
    char cmd[10];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%9s", cmd);
        if (strcmp(cmd, "add") == 0) {
            scanf("%99s", words[top]);
            top++;
        } else if (strcmp(cmd, "undo") == 0) {
            if (top > 0) {
                top--;
            }
        } else if (top == 0) {
            printf("(empty)\n");
        } else {
            for (int k = 0; k < top; k++) {
                if (k > 0) {
                    printf(" ");
                }
                printf("%s", words[k]);
            }
            printf("\n");
        }
    }
    return 0;
}
