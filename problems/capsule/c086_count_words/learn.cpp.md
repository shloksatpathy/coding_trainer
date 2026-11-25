**Learn · words**

`>>` skips spaces and reads one word. `while (std::cin >> w)` reads word after word until the input runs out.

```cpp
std::string w;
while (std::cin >> w) {
    std::cout << w << "\n";
}
```

With the input `  to be  ` this prints `to` and `be` on two lines.
