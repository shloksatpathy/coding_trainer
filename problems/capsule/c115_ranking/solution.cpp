#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int score;
};

bool before(const Student &a, const Student &b) {
    if (a.score != b.score) {
        return a.score > b.score;
    }
    return a.name < b.name;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<Student> s(n);
    for (int i = 0; i < n; i++) {
        std::cin >> s[i].name >> s[i].score;
    }
    std::sort(s.begin(), s.end(), before);
    for (int i = 0; i < n; i++) {
        std::cout << i + 1 << ". " << s[i].name << " " << s[i].score << "\n";
    }
    return 0;
}
