import sys

def operation(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

t = int(sys.stdin.readline())

n_list = []
for _ in range(t):
    n_list.append(int(sys.stdin.readline().strip()))

# 입력 정수 하나씩 반복
for i in n_list:
    r_list = []
    r_list.append(i)
    while i != 1:
        i = operation(i)
        r_list.append(i)
    
    print(max(r_list))