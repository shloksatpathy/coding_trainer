#include <stdio.h>

void back(char w[], int i) {
    if (w[i] == '\0') {
        return;
    }
    back(w, i + 1);
    printf("%c", w[i]);
}

int main(void) {
    char w[100];
    scanf("%99s", w);
    back(w, 0);
    printf("\n");
    return 0;
}
