#include <stdio.h>
#include <string.h>

int main(void) {
    char w[100], longest[100], shortest[100];
    int count = 0, total = 0;
    while (scanf("%99s", w) == 1) {
        int n = strlen(w);
        if (count == 0 || n > (int)strlen(longest)) {
            strcpy(longest, w);
        }
        if (count == 0 || n < (int)strlen(shortest)) {
            strcpy(shortest, w);
        }
        total += n;
        count++;
    }
    printf("words: %d\n", count);
    printf("longest: %s\n", longest);
    printf("shortest: %s\n", shortest);
    printf("average: %.2f\n", (double)total / count);
    return 0;
}
