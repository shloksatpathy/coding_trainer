**Learn · returning a value**

The type in front of the function's name is the type of the value it returns; `return value;` ends the function and hands the value back.

```cpp
int double_it(int x) {
    return x * 2;
}

int main() {
    int y = double_it(5) + 1;
    std::cout << y << "\n";
    return 0;
}
```

prints `11`.
