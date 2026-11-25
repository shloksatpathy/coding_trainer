**Learn · sorting numbers with the library**

`qsort(a, n, sizeof a[0], compare)` from `<stdlib.h>` sorts an array with your `compare` function (see C115). Return -1, 0 or 1 rather than `x - y`, which can overflow for large values.

```c
int compare(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    if (x < y) {
        return -1;
    }
    if (x > y) {
        return 1;
    }
    return 0;
}

// int a[3] = {3, 1, 2};
// qsort(a, 3, sizeof a[0], compare);  // 1 2 3
```
