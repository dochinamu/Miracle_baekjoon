import sys 
n,m = map(int, sys.stdin.readline().split())

castle = []

for _ in range(n):
    castle.append(sys.stdin.readline().strip())

row_count, col_count = 0, 0

for i in range(n):
    if 'X' not in castle[i]:
        row_count += 1


for j in range(m):
    for i in range(n):
        if 'X' not in castle[i][j]:
            col_count += 1

print(max(row_count, col_count))