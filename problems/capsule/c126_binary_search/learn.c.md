**Learn · binary search**

Keep a range `lo..hi` where the value must be. Look at the middle: if it is the value you are done; if it is smaller, the value can only be to the right (`lo = mid + 1`), otherwise to the left (`hi = mid - 1`). When the range is empty, the value isn't there.

```c
// a = {2, 4, 6, 8}, looking for 6:
// lo=0 hi=3 mid=1: a[1]=4 < 6, so lo=2
// lo=2 hi=3 mid=2: a[2]=6, found at index 2
```
