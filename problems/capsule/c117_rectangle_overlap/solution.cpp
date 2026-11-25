#include <algorithm>
#include <iostream>

struct Rect {
    int x1, y1, x2, y2;
};

int overlap_area(Rect a, Rect b) {
    int w = std::min(a.x2, b.x2) - std::max(a.x1, b.x1);
    int h = std::min(a.y2, b.y2) - std::max(a.y1, b.y1);
    if (w <= 0 || h <= 0) {
        return 0;
    }
    return w * h;
}

int main() {
    Rect a, b;
    std::cin >> a.x1 >> a.y1 >> a.x2 >> a.y2;
    std::cin >> b.x1 >> b.y1 >> b.x2 >> b.y2;
    std::cout << overlap_area(a, b) << "\n";
    return 0;
}
