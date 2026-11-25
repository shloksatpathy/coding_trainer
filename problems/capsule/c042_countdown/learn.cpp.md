**Learn · while loops**

`while (condition) { ... }` checks the condition before every round and stops as soon as it is false. `n--` subtracts 1.

```cpp
int x = 1;
while (x < 100) {
    x *= 3;
}
std::cout << x << "\n";
```

prints `243`, the first power of 3 that is 100 or more.
