**Learn · keeping a copy of a word**

Assigning a `std::string` copies the text: `best = w` still holds the word after `w` changes.

```cpp
std::string best, w;
while (std::cin >> w) {
    best = w;
}
std::cout << best << "\n";
```

keeps the last word.
