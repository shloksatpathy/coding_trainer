#include <iostream>
#include <string>
#include <vector>

int main() {
    int n;
    std::size_t head = 0;
    std::cin >> n;
    std::vector<std::string> queue;
    std::string cmd, name;
    for (int i = 0; i < n; i++) {
        std::cin >> cmd;
        if (cmd == "join") {
            std::cin >> name;
            queue.push_back(name);
        } else if (head < queue.size()) {
            std::cout << "served " << queue[head] << "\n";
            head++;
        } else {
            std::cout << "nobody waiting\n";
        }
    }
    std::cout << "waiting:";
    if (head == queue.size()) {
        std::cout << " none";
    }
    for (std::size_t k = head; k < queue.size(); k++) {
        std::cout << " " << queue[k];
    }
    std::cout << "\n";
    return 0;
}
