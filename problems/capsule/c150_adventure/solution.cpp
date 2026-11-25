#include <iostream>
#include <string>

const std::string ROOMS[5] = {"hall", "kitchen", "library", "garden", "vault"};
const std::string DIRS[4] = {"north", "east", "south", "west"};
const int EXITS[5][4] = {{2, -1, 3, 1}, {-1, 0, -1, -1}, {-1, 4, 0, -1}, {0, -1, -1, -1}, {-1, -1, -1, -1}};
const int VAULT = 4;

int main() {
    int room = 0, key_room = 3, n;
    bool has_key = false;
    std::string cmd, arg;
    std::cin >> n;
    for (int i = 0; i < n && room != VAULT; i++) {
        std::cin >> cmd;
        if (cmd == "go") {
            std::cin >> arg;
            int d = 0;
            while (d < 4 && DIRS[d] != arg) {
                d++;
            }
            if (d == 4 || EXITS[room][d] == -1) {
                std::cout << "You can't go " << arg << ".\n";
            } else if (EXITS[room][d] == VAULT && !has_key) {
                std::cout << "The vault is locked.\n";
            } else {
                room = EXITS[room][d];
                std::cout << "You are in the " << ROOMS[room] << ".\n";
                if (room == VAULT) {
                    std::cout << "You found the treasure!\n";
                }
            }
        } else if (cmd == "take") {
            std::cin >> arg;
            if (key_room == room) {
                std::cout << "You take the key.\n";
                has_key = true;
                key_room = -1;
            } else {
                std::cout << "There is no key here.\n";
            }
        } else {
            std::cout << ROOMS[room] << ": exits";
            for (int d = 0; d < 4; d++) {
                if (EXITS[room][d] != -1) {
                    std::cout << " " << DIRS[d];
                }
            }
            if (key_room == room) {
                std::cout << " (key here)";
            }
            std::cout << "\n";
        }
    }
    if (room != VAULT) {
        std::cout << "You give up in the " << ROOMS[room] << ".\n";
    }
    return 0;
}
