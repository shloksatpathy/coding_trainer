**Learn · more than two cases**

`else if` adds another condition, checked only when the ones before it were false.

```cpp
if (t < 10) {
    std::cout << "cold\n";
} else if (t < 25) {
    std::cout << "mild\n";
} else {
    std::cout << "hot\n";
}
```
