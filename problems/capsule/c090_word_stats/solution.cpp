#include <iomanip>
#include <iostream>
#include <string>

int main() {
    std::string w, longest, shortest;
    int count = 0, total = 0;
    while (std::cin >> w) {
        if (count == 0 || w.size() > longest.size()) {
            longest = w;
        }
        if (count == 0 || w.size() < shortest.size()) {
            shortest = w;
        }
        total += w.size();
        count++;
    }
    std::cout << "words: " << count << "\n";
    std::cout << "longest: " << longest << "\n";
    std::cout << "shortest: " << shortest << "\n";
    std::cout << std::fixed << std::setprecision(2) << "average: " << (double)total / count << "\n";
    return 0;
}
