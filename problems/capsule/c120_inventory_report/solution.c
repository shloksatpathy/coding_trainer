#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Line {
    char name[11];
    long long total;
    int qty;
};

int compare(const void *a, const void *b) {
    const struct Line *x = a, *y = b;
    if (x->total < y->total) {
        return 1;
    }
    if (x->total > y->total) {
        return -1;
    }
    return strcmp(x->name, y->name);
}

int main(void) {
    int n;
    struct Line lines[1000];
    long long grand = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        long long price;
        scanf("%10s %lld %d", lines[i].name, &price, &lines[i].qty);
        lines[i].total = price * lines[i].qty;
        grand += lines[i].total;
    }
    qsort(lines, n, sizeof lines[0], compare);
    for (int i = 0; i < n; i++) {
        printf("%-10s%5d%7lld.%02lld\n", lines[i].name, lines[i].qty, lines[i].total / 100, lines[i].total % 100);
    }
    printf("%-15s%7lld.%02lld\n", "TOTAL", grand / 100, grand % 100);
    return 0;
}
