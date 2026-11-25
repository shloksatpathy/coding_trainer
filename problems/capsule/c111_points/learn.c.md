**Learn · records**

`struct Point { ... };` defines a new type made of named fields; `struct Point p = {3, 4};` creates one and `p.x` is a field.

```c
struct Point {
    int x;
    int y;
};

int main(void) {
    struct Point p = {3, 4};
    printf("%d\n", p.x + p.y);
    return 0;
}
```

prints `7`.
