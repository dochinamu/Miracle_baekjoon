import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().split())

    d1 = pow(a, 2) + pow(b+c, 2)
    d2 = pow(b, 2) + pow(a+c, 2)
    d3 = pow(c, 2) + pow(a+b, 2)
    print(min(d1, d2, d3))