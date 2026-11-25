#include <stdio.h>

char buf[11];

void gen(int pos, int n) {
    if (pos == n) {
        printf("%s\n", buf);
        return;
    }
    buf[pos] = '0';
    gen(pos + 1, n);
    buf[pos] = '1';
    gen(pos + 1, n);
}

int main(void) {
    int n;
    scanf("%d", &n);
    buf[n] = '\0';
    gen(0, n);
    return 0;
}
