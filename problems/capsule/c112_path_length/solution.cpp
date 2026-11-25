#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

struct Point {
    int x;
    int y;
};

double distance(Point p, Point q) {
    double dx = q.x - p.x, dy = q.y - p.y;
    return std::sqrt(dx * dx + dy * dy);
}

int main() {
    int n;
    std::cin >> n;
    std::vector<Point> pts(n);
    for (int i = 0; i < n; i++) {
        std::cin >> pts[i].x >> pts[i].y;
    }
    double total = 0;
    for (int i = 1; i < n; i++) {
        total += distance(pts[i - 1], pts[i]);
    }
    std::cout << std::fixed << std::setprecision(2) << total << "\n";
    return 0;
}
