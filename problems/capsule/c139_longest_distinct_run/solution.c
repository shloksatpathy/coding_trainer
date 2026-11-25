#include <stdio.h>
#include <string.h>

int main(void) {
    char line[1000];
    fgets(line, sizeof line, stdin);
    line[strcspn(line, "\n")] = '\0';
    int last[256];
    for (int i = 0; i < 256; i++) {
        last[i] = -1;
    }
    int start = 0, best = 0;
    for (int i = 0; line[i] != '\0'; i++) {
        unsigned char ch = line[i];
        if (last[ch] >= start) {
            start = last[ch] + 1;
        }
        last[ch] = i;
        if (i - start + 1 > best) {
            best = i - start + 1;
        }
    }
    printf("%d\n", best);
    return 0;
}
