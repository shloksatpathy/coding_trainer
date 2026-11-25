#include <stdio.h>

int main(void) {
    const int SECONDS_PER_MINUTE = 60;
    const int MS_PER_SECOND = 1000;
    int m;
    scanf("%d", &m);
    int s = m * SECONDS_PER_MINUTE;
    printf("%d seconds\n", s);
    printf("%d milliseconds\n", s * MS_PER_SECOND);
    return 0;
}
