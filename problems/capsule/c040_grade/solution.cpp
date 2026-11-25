#include <iostream>

int main() {
    int s;
    std::cin >> s;
    if (s < 0 || s > 100) {
        std::cout << "invalid\n";
    } else {
        char letter;
        if (s >= 90) {
            letter = 'A';
        } else if (s >= 80) {
            letter = 'B';
        } else if (s >= 70) {
            letter = 'C';
        } else if (s >= 60) {
            letter = 'D';
        } else {
            letter = 'F';
        }
        if (s >= 60) {
            std::cout << letter << " pass\n";
        } else {
            std::cout << letter << " fail\n";
        }
    }
    return 0;
}
