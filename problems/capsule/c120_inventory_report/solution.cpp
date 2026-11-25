#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

struct Line {
    std::string name;
    long long total;
    int qty;
};

bool before(const Line &a, const Line &b) {
    if (a.total != b.total) {
        return a.total > b.total;
    }
    return a.name < b.name;
}

std::string money(long long cents) {
    std::string c = std::to_string(cents % 100);
    if (c.size() == 1) {
        c = "0" + c;
    }
    return std::to_string(cents / 100) + "." + c;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<Line> lines(n);
    long long grand = 0;
    for (int i = 0; i < n; i++) {
        long long price;
        std::cin >> lines[i].name >> price >> lines[i].qty;
        lines[i].total = price * lines[i].qty;
        grand += lines[i].total;
    }
    std::sort(lines.begin(), lines.end(), before);
    for (int i = 0; i < n; i++) {
        std::cout << std::left << std::setw(10) << lines[i].name << std::right << std::setw(5) << lines[i].qty
                  << std::setw(10) << money(lines[i].total) << "\n";
    }
    std::cout << std::left << std::setw(15) << "TOTAL" << std::right << std::setw(10) << money(grand) << "\n";
    return 0;
}
