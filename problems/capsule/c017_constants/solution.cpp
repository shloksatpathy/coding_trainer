#include <iostream>

int main() {
    const int SECONDS_PER_MINUTE = 60;
    const int MS_PER_SECOND = 1000;
    int m;
    std::cin >> m;
    int s = m * SECONDS_PER_MINUTE;
    std::cout << s << " seconds\n";
    std::cout << s * MS_PER_SECOND << " milliseconds\n";
    return 0;
}
