#include <stdbool.h>
#include <stdio.h>

bool is_prime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main(void) {
    int a, b, found = 0;
    scanf("%d %d", &a, &b);
    for (int x = a; x <= b; x++) {
        if (is_prime(x)) {
            if (found > 0) {
                printf(" ");
            }
            printf("%d", x);
            found++;
        }
    }
    if (found == 0) {
        printf("none\n");
    } else {
        printf("\n");
    }
    return 0;
}
