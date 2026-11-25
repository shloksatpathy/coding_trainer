#include <stdio.h>

char opener(char close) {
    if (close == ')') {
        return '(';
    }
    if (close == ']') {
        return '[';
    }
    return '{';
}

int main(void) {
    char line[1000], stack[1000];
    int top = 0, ok = 1;
    fgets(line, sizeof line, stdin);
    for (int i = 0; line[i] != '\0' && ok; i++) {
        char ch = line[i];
        if (ch == '(' || ch == '[' || ch == '{') {
            stack[top] = ch;
            top++;
        } else if (ch == ')' || ch == ']' || ch == '}') {
            if (top == 0 || stack[top - 1] != opener(ch)) {
                ok = 0;
            } else {
                top--;
            }
        }
    }
    if (ok && top == 0) {
        printf("yes\n");
    } else {
        printf("no\n");
    }
    return 0;
}
