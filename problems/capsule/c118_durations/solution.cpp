#include <iomanip>
#include <iostream>

struct Time {
    int h, m;
};

int to_minutes(Time t) {
    return t.h * 60 + t.m;
}

int main() {
    Time a, b;
    char colon;
    std::cin >> a.h >> colon >> a.m >> b.h >> colon >> b.m;
    int d = to_minutes(b) - to_minutes(a);
    std::cout << d / 60 << ":" << std::setfill('0') << std::setw(2) << d % 60 << "\n";
    return 0;
}
