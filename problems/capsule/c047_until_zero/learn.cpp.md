**Learn · leaving a loop with break**

`while (true)` loops forever; `break` leaves the loop right away.

```cpp
int x;
while (true) {
    std::cin >> x;
    if (x < 0) {
        break;
    }
    std::cout << x * 2 << "\n";
}
```

doubles numbers until the first negative one.
