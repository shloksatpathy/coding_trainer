**Learn · reading two numbers**

One `scanf` can read several values: one `%d` and one `&variable` for each.

```c
int w, h;
scanf("%d %d", &w, &h);
printf("%d\n", w * h);
```

With the input `4 5` this prints `20`.
