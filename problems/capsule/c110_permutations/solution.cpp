#include <iostream>
#include <vector>

void perm(std::vector<int> &cur, std::vector<bool> &used, int n) {
    if ((int)cur.size() == n) {
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                std::cout << " ";
            }
            std::cout << cur[i];
        }
        std::cout << "\n";
        return;
    }
    for (int x = 1; x <= n; x++) {
        if (!used[x]) {
            used[x] = true;
            cur.push_back(x);
            perm(cur, used, n);
            cur.pop_back();
            used[x] = false;
        }
    }
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> cur;
    std::vector<bool> used(n + 1, false);
    perm(cur, used, n);
    return 0;
}
