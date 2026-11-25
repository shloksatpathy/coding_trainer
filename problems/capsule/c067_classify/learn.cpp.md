**Learn · returning early, returning text**

A `return` ends the function at once, so the checks after it need no `else`. A function can return a `std::string` like any other value.

```cpp
std::string size(int n) {
    if (n < 10) {
        return "short";
    }
    return "long";
}
```
