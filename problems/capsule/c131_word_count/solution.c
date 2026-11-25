#include <stdio.h>
#include <string.h>

char words[1000][100];
int counts[1000];
int size = 0;

int find(char w[]) {
    for (int i = 0; i < size; i++) {
        if (strcmp(words[i], w) == 0) {
            return i;
        }
    }
    return -1;
}

int main(void) {
    int n;
    char w[100];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%99s", w);
        int k = find(w);
        if (k == -1) {
            k = size;
            strcpy(words[k], w);
            counts[k] = 0;
            size++;
        }
        counts[k]++;
    }
    for (int i = 0; i < size; i++) {
        printf("%s: %d\n", words[i], counts[i]);
    }
    return 0;
}
