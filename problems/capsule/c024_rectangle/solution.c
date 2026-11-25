#include <stdio.h>

int main(void) {
    double w, h;
    scanf("%lf %lf", &w, &h);
    printf("area: %.2f\n", w * h);
    printf("perimeter: %.2f\n", 2 * (w + h));
    return 0;
}
