**Learn · returning a value**

The type in front of the function's name is the type of the value it returns; `return value;` ends the function and hands the value back.

```c
int double_it(int x) {
    return x * 2;
}

int main(void) {
    int y = double_it(5) + 1;
    printf("%d\n", y);
    return 0;
}
```

prints `11`.
