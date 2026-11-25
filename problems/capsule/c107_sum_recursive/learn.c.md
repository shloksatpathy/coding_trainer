**Learn · passing an array to a function**

An array parameter is written `int a[]`. C doesn't pass the length along, so pass `n` too.

```c
int first(int a[]) {
    return a[0];
}
```
