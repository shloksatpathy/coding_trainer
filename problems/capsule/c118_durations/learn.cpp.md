**Learn · reading values with separators**

Read the separator into a `char` you then ignore: `std::cin >> h >> colon >> m` reads `09:15`.

```cpp
int h, m;
char colon;
std::cin >> h >> colon >> m;
std::cout << h << " " << m << "\n";
```

prints `9 15`.
