#include <stdio.h>

int main(void) {
    int coins[8] = {200, 100, 50, 20, 10, 5, 2, 1};
    int amount, total = 0;
    scanf("%d", &amount);
    for (int i = 0; i < 8; i++) {
        int k = amount / coins[i];
        if (k > 0) {
            printf("%d x %d\n", coins[i], k);
            amount -= k * coins[i];
            total += k;
        }
    }
    printf("coins: %d\n", total);
    return 0;
}
