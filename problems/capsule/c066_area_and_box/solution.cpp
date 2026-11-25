#include <iostream>

int area(int w, int h) {
    return w * h;
}

void draw_box(int w, int h) {
    for (int r = 0; r < h; r++) {
        for (int col = 0; col < w; col++) {
            std::cout << "*";
        }
        std::cout << "\n";
    }
}

int main() {
    int w, h;
    std::cin >> w >> h;
    std::cout << "area: " << area(w, h) << "\n";
    draw_box(w, h);
    return 0;
}
