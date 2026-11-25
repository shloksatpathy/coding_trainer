**Learn · sorting with your own rule**

`qsort(array, count, size of one element, compare)` from `<stdlib.h>` sorts with your function `compare(a, b)`, which returns a negative number if `a` goes first, a positive one if `b` goes first and 0 if they are equal. It receives `const void *` pointers: assign them to `const struct Student *` and use `->` to reach fields. `strcmp` compares two texts the same way.

```c
int by_value_desc(const void *a, const void *b) {
    const int *x = a, *y = b;
    return *y - *x;
}

// int v[3] = {2, 9, 4};
// qsort(v, 3, sizeof v[0], by_value_desc);  // 9 4 2
```
