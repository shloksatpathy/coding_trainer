#include <iomanip>
#include <iostream>
#include <string>

struct Report {
    std::string name;
    int scores[3];
};

int main() {
    Report r;
    std::cin >> r.name >> r.scores[0] >> r.scores[1] >> r.scores[2];
    int total = 0, best = r.scores[0];
    for (int i = 0; i < 3; i++) {
        total += r.scores[i];
        if (r.scores[i] > best) {
            best = r.scores[i];
        }
    }
    std::cout << r.name << ": total " << total << ", average " << std::fixed << std::setprecision(2) << total / 3.0 << ", best " << best << "\n";
    return 0;
}
