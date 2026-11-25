#include <iostream>
#include <string>
#include <vector>

int main() {
    int r, c;
    std::cin >> r >> c;
    std::vector<std::string> g(r);
    for (int i = 0; i < r; i++) {
        std::cin >> g[i];
    }
    std::string moves;
    std::cin >> moves;
    int row = 0, col = 0, moved = 0;
    for (std::size_t i = 0; i < moves.size(); i++) {
        int nr = row, nc = col;
        if (moves[i] == 'U') {
            nr--;
        } else if (moves[i] == 'D') {
            nr++;
        } else if (moves[i] == 'L') {
            nc--;
        } else {
            nc++;
        }
        if (nr >= 0 && nr < r && nc >= 0 && nc < c && g[nr][nc] == '.') {
            row = nr;
            col = nc;
            moved++;
        }
    }
    std::cout << "at " << row + 1 << " " << col + 1 << "\n";
    std::cout << "moved: " << moved << "\n";
    return 0;
}
