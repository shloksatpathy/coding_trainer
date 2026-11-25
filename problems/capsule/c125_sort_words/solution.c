#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char words[1000][100];

int compare(const void *p, const void *q) {
    const char *x = p, *y = q;
    int lx = strlen(x), ly = strlen(y);
    if (lx != ly) {
        return lx - ly;
    }
    return strcmp(x, y);
}

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%99s", words[i]);
    }
    qsort(words, n, sizeof words[0], compare);
    for (int i = 0; i < n; i++) {
        printf("%s\n", words[i]);
    }
    return 0;
}
