#include <stdio.h>

struct Student {
    char name[100];
    int score;
};

int main(void) {
    int n;
    struct Student s[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%99s %d", s[i].name, &s[i].score);
    }
    int top = 0, total = 0, found = 0;
    for (int i = 0; i < n; i++) {
        total += s[i].score;
        if (s[i].score > s[top].score) {
            top = i;
        }
    }
    printf("top: %s (%d)\n", s[top].name, s[top].score);
    printf("average: %.2f\n", (double)total / n);
    printf("above:");
    for (int i = 0; i < n; i++) {
        if (s[i].score * n > total) {
            printf(" %s", s[i].name);
            found++;
        }
    }
    if (found == 0) {
        printf(" none");
    }
    printf("\n");
    return 0;
}
