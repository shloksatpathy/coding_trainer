**Learn · records**

`struct Point { ... };` defines a new type made of named fields; `Point p = {3, 4};` creates one and `p.x` is a field.

```cpp
struct Point {
    int x;
    int y;
};

int main() {
    Point p = {3, 4};
    std::cout << p.x + p.y << "\n";
    return 0;
}
```

prints `7`.
