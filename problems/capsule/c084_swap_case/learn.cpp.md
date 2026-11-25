**Learn · looking at each character**

Loop over the indexes (`std::size_t` is the type of `size()`). `<cctype>` has `std::isupper`, `std::islower`, `std::isdigit` to test a character and `std::toupper`, `std::tolower` to convert it; they return an `int`, so convert back with `(char)`.

```cpp
std::string text = "a1B";
for (std::size_t i = 0; i < text.size(); i++) {
    if (std::isupper(text[i])) {
        std::cout << text[i] << " is uppercase\n";
    }
}
```

prints `B is uppercase`.
