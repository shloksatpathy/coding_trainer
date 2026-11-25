#include <stdio.h>

void down_up(int n) {
    if (n == 0) {
        return;
    }
    printf("%d\n", n);
    down_up(n - 1);
    printf("%d\n", n);
}

int main(void) {
    int n;
    scanf("%d", &n);
    down_up(n);
    return 0;
}
