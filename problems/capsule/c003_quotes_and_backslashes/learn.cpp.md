**Learn · escapes**

A `"` would end the text, so inside quotes you write `\"` for a quote. A `\` starts an escape (like `\n`), so you write `\\` for one backslash.

```cpp
std::cout << "A \"quoted\" word\n";
std::cout << "one\\two\n";
```

prints `A "quoted" word` and `one\two`.
