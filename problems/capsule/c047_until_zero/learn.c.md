**Learn · leaving a loop with break**

`while (1)` loops forever; `break` leaves the loop right away.

```c
int x;
while (1) {
    scanf("%d", &x);
    if (x < 0) {
        break;
    }
    printf("%d\n", x * 2);
}
```

doubles numbers until the first negative one.
