#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string line;
    std::getline(std::cin, line);
    std::vector<int> last(256, -1);
    int start = 0, best = 0;
    for (int i = 0; i < (int)line.size(); i++) {
        unsigned char ch = line[i];
        if (last[ch] >= start) {
            start = last[ch] + 1;
        }
        last[ch] = i;
        if (i - start + 1 > best) {
            best = i - start + 1;
        }
    }
    std::cout << best << "\n";
    return 0;
}
