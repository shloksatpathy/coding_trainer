#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

int count[26];

int compare(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    if (count[x] != count[y]) {
        return count[y] - count[x];
    }
    return x - y;
}

int main(void) {
    char line[1000];
    fgets(line, sizeof line, stdin);
    for (int i = 0; line[i] != '\0'; i++) {
        if (isalpha(line[i])) {
            count[tolower(line[i]) - 'a']++;
        }
    }
    int order[26];
    for (int i = 0; i < 26; i++) {
        order[i] = i;
    }
    qsort(order, 26, sizeof order[0], compare);
    for (int i = 0; i < 26; i++) {
        if (count[order[i]] > 0) {
            printf("%c: %d\n", 'a' + order[i], count[order[i]]);
        }
    }
    return 0;
}
