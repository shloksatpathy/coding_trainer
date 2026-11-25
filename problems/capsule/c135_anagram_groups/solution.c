#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char keys[1000][21], words[1000][21];
int group_of[1000];
int ngroups = 0;

int by_char(const void *p, const void *q) {
    return *(const char *)p - *(const char *)q;
}

int main(void) {
    int n;
    char w[21], key[21];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%20s", w);
        strcpy(key, w);
        qsort(key, strlen(key), 1, by_char);
        int g = 0;
        while (g < ngroups && strcmp(keys[g], key) != 0) {
            g++;
        }
        if (g == ngroups) {
            strcpy(keys[g], key);
            ngroups++;
        }
        strcpy(words[i], w);
        group_of[i] = g;
    }
    for (int g = 0; g < ngroups; g++) {
        int first = 1;
        for (int i = 0; i < n; i++) {
            if (group_of[i] == g) {
                if (!first) {
                    printf(" ");
                }
                printf("%s", words[i]);
                first = 0;
            }
        }
        printf("\n");
    }
    return 0;
}
