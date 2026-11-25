**Learn · fast lookups: hashing**

A hash table stores each key at a position computed from the key itself (its hash). If that place is taken by another key, try the next one. With a table more than twice as big as the number of keys, a lookup takes about one step. `#define SIZE 524288` gives the number a name; `& (SIZE - 1)` wraps around because SIZE is a power of two.

```c
#define SIZE 524288

long long keys[SIZE];
int used[SIZE];
int vals[SIZE];

int slot(long long key) {
    unsigned long long h = (unsigned long long)key * 11400714819323198485ull;
    int i = h >> 45;
    while (used[i] && keys[i] != key) {
        i = (i + 1) & (SIZE - 1);
    }
    return i;
}

// int k = slot(x);   where x is, or would go
// used[k]            is x there?
// used[k] = 1; keys[k] = x;   add it
```

prints no, no, yes (as false/true or 0/1).
