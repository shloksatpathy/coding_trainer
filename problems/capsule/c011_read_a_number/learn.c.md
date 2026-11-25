**Learn · variables and reading a number**

A variable has a type: `int` holds a whole number. `scanf("%d", &age)` reads a number into `age`; the `&` tells `scanf` where the variable lives.

```c
int age;
scanf("%d", &age);
printf("%d\n", age + 1);
```

With the input `41` this prints `42`.
