#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    char name[100];
    int score;
};

int compare(const void *a, const void *b) {
    const struct Student *x = a, *y = b;
    if (x->score != y->score) {
        return y->score - x->score;
    }
    return strcmp(x->name, y->name);
}

int main(void) {
    int n;
    struct Student s[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%99s %d", s[i].name, &s[i].score);
    }
    qsort(s, n, sizeof s[0], compare);
    for (int i = 0; i < n; i++) {
        printf("%d. %s %d\n", i + 1, s[i].name, s[i].score);
    }
    return 0;
}
