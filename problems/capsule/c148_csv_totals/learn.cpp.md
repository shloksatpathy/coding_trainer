**Learn · splitting a line at commas**

Put the line in a `std::stringstream` (from `<sstream>`); `std::getline(fields, part, ',')` then reads up to the next comma. `std::stoi` turns text into an `int`.

```cpp
std::stringstream fields("ann,oslo");
std::string name, city;
std::getline(fields, name, ',');
std::getline(fields, city, ',');
std::cout << city << "\n";
```
