**Learn · changing the caller's data**

`std::string &buf` (without `const`) passes the string by reference, so the function changes the caller's string.

```cpp
void set_first(std::string &buf) {
    buf[0] = 'x';
}
```
