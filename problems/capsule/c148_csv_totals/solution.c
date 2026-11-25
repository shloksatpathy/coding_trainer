#include <stdio.h>
#include <string.h>

char depts[1000][100];
int totals[1000];

int main(void) {
    int n, amount, overall = 0, size = 0;
    char name[100], dept[100];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf(" %99[^,],%99[^,],%d", name, dept, &amount);
        int k = 0;
        while (k < size && strcmp(depts[k], dept) != 0) {
            k++;
        }
        if (k == size) {
            strcpy(depts[k], dept);
            totals[k] = 0;
            size++;
        }
        totals[k] += amount;
        overall += amount;
    }
    for (int k = 0; k < size; k++) {
        printf("%s: %d\n", depts[k], totals[k]);
    }
    printf("overall: %d\n", overall);
    return 0;
}
