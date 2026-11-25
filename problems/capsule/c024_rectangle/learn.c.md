**Learn · reading decimal numbers**

Read a `double` with `%lf` (printing uses `%f`).

```c
double price;
scanf("%lf", &price);
printf("%.2f\n", price * 2);
```

With the input `1.25` this prints `2.50`.
