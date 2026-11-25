**Learn · an array of records**

An array can hold records: `struct Student s[1000];` and `s[i].score`. `scanf` can read straight into a field: `&s[i].score` (a `char` array field needs no `&`).

```c
struct Student s[2] = {{"ann", 90}, {"bob", 72}};
printf("%s\n", s[1].name);
```

prints `bob`.
