**Learn · passing an array to a function**

`const std::vector<int> &a` passes the vector by reference: no copy is made, and `const` promises not to change it.

```cpp
int first(const std::vector<int> &a) {
    return a[0];
}
```
