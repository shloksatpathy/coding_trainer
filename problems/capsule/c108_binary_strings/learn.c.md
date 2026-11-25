**Learn · changing the caller's data**

A global array (declared outside all functions) can be read and changed by every function; each call fills in its own position.

```c
char buf[11];

void set_first(void) {
    buf[0] = 'x';
}
```
