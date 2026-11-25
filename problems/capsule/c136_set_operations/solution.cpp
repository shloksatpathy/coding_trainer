#include <iostream>
#include <set>
#include <string>

std::set<int> read_set() {
    int n, x;
    std::cin >> n;
    std::set<int> s;
    for (int i = 0; i < n; i++) {
        std::cin >> x;
        s.insert(x);
    }
    return s;
}

void show(const std::string &label, const std::set<int> &s) {
    std::cout << label << ":";
    if (s.empty()) {
        std::cout << " none";
    }
    for (int x : s) {
        std::cout << " " << x;
    }
    std::cout << "\n";
}

int main() {
    std::set<int> a = read_set(), b = read_set();
    std::set<int> uni = a, both, only;
    for (int x : b) {
        uni.insert(x);
    }
    for (int x : a) {
        if (b.count(x)) {
            both.insert(x);
        } else {
            only.insert(x);
        }
    }
    show("union", uni);
    show("both", both);
    show("only first", only);
    return 0;
}
