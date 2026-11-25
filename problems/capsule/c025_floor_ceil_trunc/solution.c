#include <math.h>
#include <stdio.h>

int main(void) {
    double x;
    scanf("%lf", &x);
    printf("%d %d %d\n", (int)floor(x), (int)ceil(x), (int)x);
    return 0;
}
