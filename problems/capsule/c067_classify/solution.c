#include <stdio.h>

const char *classify(int n) {
    if (n < 0) {
        return "negative";
    }
    if (n == 0) {
        return "zero";
    }
    if (n < 10) {
        return "small";
    }
    if (n < 100) {
        return "medium";
    }
    return "large";
}

int main(void) {
    int n, x;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        printf("%s\n", classify(x));
    }
    return 0;
}
