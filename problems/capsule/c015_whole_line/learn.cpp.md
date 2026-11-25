**Learn · reading a whole line**

`>>` stops at the first space; `std::getline` reads the whole line.

```cpp
std::string line;
std::getline(std::cin, line);
std::cout << "[" << line << "]\n";
```
