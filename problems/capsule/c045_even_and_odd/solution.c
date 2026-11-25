#include <stdio.h>

int main(void) {
    int n, x, even = 0, odd = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
    printf("even: %d\n", even);
    printf("odd: %d\n", odd);
    return 0;
}
