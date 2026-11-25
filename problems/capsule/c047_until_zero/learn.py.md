**Learn · leaving a loop with break**

`while True:` loops forever; `break` leaves the loop right away.

```python
while True:
    x = int(input())
    if x < 0:
        break
    print(x * 2)
```

doubles numbers until the first negative one.
