import sys

t = int(sys.stdin.readline())
result = []

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    f_digit = pow(a, b, 10)
    result.append(f_digit)
   
for i in result:
    if i == 0:
        print(10)
    else:
        print(i)
