**Learn · functions**

A function is written outside `main`, above it. Each parameter has a type; `void` in front means the function gives nothing back. A text parameter is written `char name[]`.

```c
void show_double(int x) {
    printf("%d\n", x * 2);
}

int main(void) {
    show_double(4);
    show_double(10);
    return 0;
}
```

prints `8` and `20`.
