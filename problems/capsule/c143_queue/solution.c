#include <stdio.h>
#include <string.h>

char queue[1000][100];

int main(void) {
    int n, head = 0, tail = 0;
    char cmd[10];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%9s", cmd);
        if (strcmp(cmd, "join") == 0) {
            scanf("%99s", queue[tail]);
            tail++;
        } else if (head < tail) {
            printf("served %s\n", queue[head]);
            head++;
        } else {
            printf("nobody waiting\n");
        }
    }
    printf("waiting:");
    if (head == tail) {
        printf(" none");
    }
    for (int k = head; k < tail; k++) {
        printf(" %s", queue[k]);
    }
    printf("\n");
    return 0;
}
