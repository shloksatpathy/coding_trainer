#include <stdio.h>

int main(void) {
    int s;
    scanf("%d", &s);
    if (s < 0 || s > 100) {
        printf("invalid\n");
    } else {
        char letter;
        if (s >= 90) {
            letter = 'A';
        } else if (s >= 80) {
            letter = 'B';
        } else if (s >= 70) {
            letter = 'C';
        } else if (s >= 60) {
            letter = 'D';
        } else {
            letter = 'F';
        }
        if (s >= 60) {
            printf("%c pass\n", letter);
        } else {
            printf("%c fail\n", letter);
        }
    }
    return 0;
}
