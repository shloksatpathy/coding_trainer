#include <stdio.h>
#include <string.h>

struct Item {
    char id[100];
    int qty;
};

struct Item items[1000];
int n;

int find(char key[]) {
    for (int i = 0; i < n; i++) {
        if (strcmp(items[i].id, key) == 0) {
            return i;
        }
    }
    return -1;
}

int main(void) {
    int m, change;
    char key[100];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%99s %d", items[i].id, &items[i].qty);
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%99s %d", key, &change);
        int k = find(key);
        if (k == -1) {
            printf("unknown %s\n", key);
        } else {
            items[k].qty += change;
        }
    }
    for (int i = 0; i < n; i++) {
        printf("%s: %d\n", items[i].id, items[i].qty);
    }
    return 0;
}
