#include <stdio.h>

int main(void) {
    int n;
    long long ways[91];
    scanf("%d", &n);
    ways[0] = 1;
    ways[1] = 1;
    for (int i = 2; i <= n; i++) {
        ways[i] = ways[i - 1] + ways[i - 2];
    }
    printf("%lld\n", ways[n]);
    return 0;
}
