s = input()
i, j = 0, len(s) - 1
ok = True
while i < j:
    if not s[i].isalnum():
        i += 1
    elif not s[j].isalnum():
        j -= 1
    elif s[i].lower() != s[j].lower():
        ok = False
        break
    else:
        i += 1
        j -= 1
print("true" if ok else "false")
