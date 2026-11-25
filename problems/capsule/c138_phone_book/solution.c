#include <stdio.h>
#include <string.h>

char names[1000][100], numbers[1000][100];

int main(void) {
    int n, q;
    char name[100];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%99s %99s", names[i], numbers[i]);
    }
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        scanf("%99s", name);
        int found = -1;
        for (int i = 0; i < n; i++) {
            if (strcmp(names[i], name) == 0) {
                found = i;
            }
        }
        if (found == -1) {
            printf("%s: not found\n", name);
        } else {
            printf("%s: %s\n", name, numbers[found]);
        }
    }
    return 0;
}
