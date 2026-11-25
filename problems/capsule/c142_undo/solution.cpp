#include <iostream>
#include <string>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> words;
    std::string cmd, w;
    for (int i = 0; i < n; i++) {
        std::cin >> cmd;
        if (cmd == "add") {
            std::cin >> w;
            words.push_back(w);
        } else if (cmd == "undo") {
            if (!words.empty()) {
                words.pop_back();
            }
        } else if (words.empty()) {
            std::cout << "(empty)\n";
        } else {
            for (std::size_t k = 0; k < words.size(); k++) {
                if (k > 0) {
                    std::cout << " ";
                }
                std::cout << words[k];
            }
            std::cout << "\n";
        }
    }
    return 0;
}
