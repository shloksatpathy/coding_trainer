def gen(prefix, n):
    if len(prefix) == n:
        print(prefix)
        return
    gen(prefix + "0", n)
    gen(prefix + "1", n)


n = int(input())
gen("", n)
