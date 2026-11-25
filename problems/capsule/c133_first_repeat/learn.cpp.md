**Learn · fast lookups: hashing**

`std::unordered_set` and `std::unordered_map` are hash tables: a key's hash says where to store it, so a lookup costs about one step however many keys there are.

```cpp
std::unordered_set<long long> seen;
for (long long x : {4, 8, 4}) {
    std::cout << seen.count(x) << "\n";
    seen.insert(x);
}
```

prints no, no, yes (as false/true or 0/1).
