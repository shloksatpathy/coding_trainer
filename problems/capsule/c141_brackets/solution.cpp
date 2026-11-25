#include <iostream>
#include <string>
#include <vector>

char opener(char close) {
    if (close == ')') {
        return '(';
    }
    if (close == ']') {
        return '[';
    }
    return '{';
}

int main() {
    std::string line;
    std::getline(std::cin, line);
    std::vector<char> stack;
    bool ok = true;
    for (std::size_t i = 0; i < line.size() && ok; i++) {
        char ch = line[i];
        if (ch == '(' || ch == '[' || ch == '{') {
            stack.push_back(ch);
        } else if (ch == ')' || ch == ']' || ch == '}') {
            if (stack.empty() || stack.back() != opener(ch)) {
                ok = false;
            } else {
                stack.pop_back();
            }
        }
    }
    if (ok && stack.empty()) {
        std::cout << "yes\n";
    } else {
        std::cout << "no\n";
    }
    return 0;
}
