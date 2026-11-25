#include <stdio.h>

struct Report {
    char name[100];
    int scores[3];
};

int main(void) {
    struct Report r;
    scanf("%99s %d %d %d", r.name, &r.scores[0], &r.scores[1], &r.scores[2]);
    int total = 0, best = r.scores[0];
    for (int i = 0; i < 3; i++) {
        total += r.scores[i];
        if (r.scores[i] > best) {
            best = r.scores[i];
        }
    }
    printf("%s: total %d, average %.2f, best %d\n", r.name, total, total / 3.0, best);
    return 0;
}
