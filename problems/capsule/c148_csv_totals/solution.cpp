#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    int n, overall = 0;
    std::cin >> n;
    std::vector<std::string> depts;
    std::vector<int> totals;
    std::string line, name, dept, amount;
    std::getline(std::cin, line);
    for (int i = 0; i < n; i++) {
        std::getline(std::cin, line);
        std::stringstream fields(line);
        std::getline(fields, name, ',');
        std::getline(fields, dept, ',');
        std::getline(fields, amount, ',');
        std::size_t k = 0;
        while (k < depts.size() && depts[k] != dept) {
            k++;
        }
        if (k == depts.size()) {
            depts.push_back(dept);
            totals.push_back(0);
        }
        totals[k] += std::stoi(amount);
        overall += std::stoi(amount);
    }
    for (std::size_t k = 0; k < depts.size(); k++) {
        std::cout << depts[k] << ": " << totals[k] << "\n";
    }
    std::cout << "overall: " << overall << "\n";
    return 0;
}
