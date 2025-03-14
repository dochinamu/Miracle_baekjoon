import sys

def recursion(s, l, r, cnt):
    if l >= r:
        return 1, cnt+1
    elif s[l] != s[r]:
        return 0, cnt+1
    else:
        return recursion(s, l + 1, r - 1, cnt+1)

def is_palindrome(s):
    return recursion(s, 0, len(s) - 1, 0)

T = int(sys.stdin.readline().strip())
for _ in range(T):
    i = sys.stdin.readline().strip()
    anw, count = is_palindrome(i)
    print(anw, count)