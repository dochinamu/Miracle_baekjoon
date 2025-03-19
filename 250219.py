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
        # 적당한 정도의 큰 수와 계속 업데이트되는 값을 min 함수에 넣어, 최소값을 추출하는 방법
        # 대신 초기화를 꼭 해줘야 한다
        res = min(res, cut(i, j))

print(res)