# C116 · Stock updates

The first line has `n` (1 ≤ n ≤ 1000); each of the next `n` lines has an item ID (one word) and a quantity. Then comes `m`, and `m` updates `ID change`. Apply each update to the item with that ID; if there is no such item, print `unknown ID` at that moment. At the end print every item as `ID: quantity`, in the original order.

**Example**

Input (also in `in.txt`):
```
3
apple 5
pear 2
fig 0
4
pear 3
fig 7
kiwi 1
apple -5
```
Output:
```
unknown kiwi
apple: 0
pear: 5
fig: 7
```

**Focus:** a lookup function that searches the records by a key and returns the position, or -1 when it isn't there.
