#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int score;
};

int main() {
    int n;
    std::cin >> n;
    std::vector<Student> s(n);
    for (int i = 0; i < n; i++) {
        std::cin >> s[i].name >> s[i].score;
    }
    int top = 0, total = 0, found = 0;
    for (int i = 0; i < n; i++) {
        total += s[i].score;
        if (s[i].score > s[top].score) {
            top = i;
        }
    }
    std::cout << "top: " << s[top].name << " (" << s[top].score << ")\n";
    std::cout << std::fixed << std::setprecision(2) << "average: " << (double)total / n << "\n";
    std::cout << "above:";
    for (int i = 0; i < n; i++) {
        if (s[i].score * n > total) {
            std::cout << " " << s[i].name;
            found++;
        }
    }
    if (found == 0) {
        std::cout << " none";
    }
    std::cout << "\n";
    return 0;
}
