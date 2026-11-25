**Learn · maps**

`std::unordered_map<std::string, int>` (from `<unordered_map>`) maps keys to values: `m[key]` reads or creates a value (starting at 0), `m.count(key)` is 1 if the key is there. It doesn't keep any order, so remember the first-seen order separately.

```cpp
std::unordered_map<std::string, int> age;
age["ann"] = 30;
std::cout << age.count("ann") << " " << age.count("bob") << "\n";
```
