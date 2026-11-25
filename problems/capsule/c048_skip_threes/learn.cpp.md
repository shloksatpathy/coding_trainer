**Learn · skipping a round with continue**

`continue` skips the rest of this round and goes on with the next one.

```cpp
for (int i = 1; i < 10; i++) {
    if (i % 2 == 0) {
        continue;
    }
    std::cout << i << "\n";
}
```

prints only the odd numbers 1, 3, 5, 7, 9.
