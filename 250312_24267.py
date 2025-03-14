import sys

def count(n):
    return (n*(n-1)*(n-2)//6)

n = int(sys.stdin.readline())

print(count(n))
print(3)