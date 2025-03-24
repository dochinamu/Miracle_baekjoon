import sys


# 사탕 가격, 0의 개수
c, k = map(int, sys.stdin.readline().split())


if k == 0:
    print(c)
else:
    if c%10**k >= 5 * 10**(k-1):
        print(c%10**k + (10**k-(c%(10**k))))
    else:
        print(c - c%10**k)
    