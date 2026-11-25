#include <iostream>

int main() {
    int w, h;
    std::cin >> w >> h;
    for (int r = 0; r < h; r++) {
        for (int col = 0; col < w; col++) {
            std::cout << "#";
        }
        std::cout << "\n";
    }
    return 0;
}
