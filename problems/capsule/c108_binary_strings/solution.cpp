#include <iostream>
#include <string>

void gen(std::string &buf, std::size_t pos) {
    if (pos == buf.size()) {
        std::cout << buf << "\n";
        return;
    }
    buf[pos] = '0';
    gen(buf, pos + 1);
    buf[pos] = '1';
    gen(buf, pos + 1);
}

int main() {
    int n;
    std::cin >> n;
    std::string buf(n, '0');
    gen(buf, 0);
    return 0;
}
