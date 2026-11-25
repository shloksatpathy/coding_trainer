**Learn · an array of records**

A vector can hold records: `std::vector<Student> s(n);` and `s[i].score`.

```cpp
std::vector<Student> s = {{"ann", 90}, {"bob", 72}};
std::cout << s[1].name << "\n";
```

prints `bob`.
