**Learn · constants**

`const` makes a variable read-only: assigning to it again is a compile error.

```c
const int HOURS_PER_DAY = 24;
int days;
scanf("%d", &days);
printf("%d\n", days * HOURS_PER_DAY);
```
