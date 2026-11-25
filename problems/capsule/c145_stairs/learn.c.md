**Learn · remembering answers**

Dynamic programming solves a problem from smaller versions of itself, like recursion, but stores each answer in an array so it is computed once.

```c
// ways[0] = 1 (already at the top)
// ways[1] = 1
// ways[2] = ways[1] + ways[0] = 2
// ways[3] = ways[2] + ways[1] = 3
```
