#include <iostream>
#include <string>

std::string g[3];

bool wins(char p) {
    for (int i = 0; i < 3; i++) {
        if (g[i][0] == p && g[i][1] == p && g[i][2] == p) {
            return true;
        }
        if (g[0][i] == p && g[1][i] == p && g[2][i] == p) {
            return true;
        }
    }
    if (g[0][0] == p && g[1][1] == p && g[2][2] == p) {
        return true;
    }
    return g[0][2] == p && g[1][1] == p && g[2][0] == p;
}

int main() {
    for (int i = 0; i < 3; i++) {
        std::cin >> g[i];
    }
    bool full = true;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (g[i][j] == '.') {
                full = false;
            }
        }
    }
    if (wins('X')) {
        std::cout << "X wins\n";
    } else if (wins('O')) {
        std::cout << "O wins\n";
    } else if (full) {
        std::cout << "draw\n";
    } else {
        std::cout << "in progress\n";
    }
    return 0;
}
