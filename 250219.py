chess=[['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

# n,m input
n, m = map(int, input().split())
res = m* m

# total board input
total = []
for i in range(n):
    total.append(list(map(str, input().strip())))

def cut(x,y):
    cnt=0
    for i in range(8):
        for j in range(8):
            if chess[i][j] != total[i+x][j+y]:
                cnt += 1
    if cnt > 64-cnt:
        return 64-cnt
    else:
        return cnt

for i in range(n-7):
    for j in range(m-7):
        res = min(res, cut(i, j))

print(res)

    