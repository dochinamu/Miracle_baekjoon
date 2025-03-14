import sys 
n,m = map(int, sys.stdin.readline().split())

security = []
for _ in range (n):
    security.append(sys.stdin.readline().strip())

cnt = 0 
  
for i in security:
    if 'X' not in i:
        cnt += 1
    else:
        vertical = []
        for j in i:
            vertical.append(security[i][j])
        if 


        cnt += 1

print(cnt)