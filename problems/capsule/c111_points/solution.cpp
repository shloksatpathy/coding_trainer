#include <cstdlib>
#include <iostream>

struct Point {
    int x;
    int y;
};

int main() {
    Point p, q;
    std::cin >> p.x >> p.y >> q.x >> q.y;
    int dx = q.x - p.x, dy = q.y - p.y;
    std::cout << "dx: " << dx << "\n";
    std::cout << "dy: " << dy << "\n";
    std::cout << "manhattan: " << std::abs(dx) + std::abs(dy) << "\n";
    return 0;
}
