import sys
 
# n, t 입력
n = int(sys.stdin.readline().strip())
t = []
for _ in range(n):
    t.append(int(sys.stdin.readline()))

# 절반 이상 공부했는가?
# [ 30, 30, 30, ..., 30]
study = []
for _ in range(n):
    study.append(30)

# 절반 이상 공부한 과목 수
cnt = 0

# 벼락치기 공부 세션 수
j = 0
for i in range(len(t)):
    if study[j] < t[i]:
        if t[i] > study[j]:
            # print('공부 시간이 부족해')
            # print('study total:', study)
            # print('study:', study[j], 't:', t[i])
            if t[i] <= study[j]*2:
                # print('그래도 절반 이상은 공부함')
                cnt += 1
            j+=1
        
    elif t[i] <= study[j]:
        # print('시간이 있다')
        study[j] -= t[i]
        # print(study)
        cnt+=1
        if study[j] <= 0:
            j+=1
            # print('j:', j)

print(cnt)