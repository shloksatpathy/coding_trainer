**Learn · maps**

C has no map in its standard library. For up to a few thousand keys, keep the keys and values in two arrays and search the keys with a loop, as below. For large inputs you need a hash table (C133) or sorting (module 13).

```c
char names[1000][100];
int ages[1000];
int size = 0;

int find(char name[]) {
    for (int i = 0; i < size; i++) {
        if (strcmp(names[i], name) == 0) {
            return i;
        }
    }
    return -1;
}
```
