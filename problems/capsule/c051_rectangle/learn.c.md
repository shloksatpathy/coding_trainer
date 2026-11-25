**Learn · a loop inside a loop**

The inner loop runs all its rounds for each round of the outer loop.

```c
for (int row = 1; row <= 2; row++) {
    for (int col = 1; col <= 3; col++) {
        printf("%d%d ", row, col);
    }
    printf("\n");
}
```

prints `11 12 13` on the first line and `21 22 23` on the second.
