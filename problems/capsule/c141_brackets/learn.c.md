**Learn · stacks**

An array and a counter `top` make a stack: `s[top] = x; top++;` pushes, `s[top - 1]` is the top, `top--` pops.

```c
int s[10], top = 0;
s[top] = 1;
top++;
s[top] = 2;
top++;
top--;
printf("%d\n", s[top]);
```

The last value pushed comes off first.
