**Learn · functions**

A function is written outside `main`, above it. Each parameter has a type; `void` in front means the function gives nothing back.

```cpp
void show_double(int x) {
    std::cout << x * 2 << "\n";
}

int main() {
    show_double(4);
    show_double(10);
    return 0;
}
```

prints `8` and `20`.
