#include <stdio.h>
#include <string.h>

int main(void) {
    char w[100];
    scanf("%99s", w);
    int i = 0, j = strlen(w) - 1, same = 1;
    while (i < j) {
        if (w[i] != w[j]) {
            same = 0;
            break;
        }
        i++;
        j--;
    }
    if (same) {
        printf("yes\n");
    } else {
        printf("no\n");
    }
    return 0;
}
