n = int(input())
rev, m = 0, n
while m > 0:
    rev = rev * 10 + m % 10
    m //= 10
print(rev, "Palindrome" if rev == n else "Not palindrome")
