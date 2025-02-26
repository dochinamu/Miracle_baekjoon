import sys 

# 입력
n, c = map(int, sys.stdin.readline().split())

freq = []
for i in range(n):
    freq.append(int(sys.stdin.readline().strip()))

'''
# *** 방법 1: 메모리 초과
# *** 폭죽쇼가 끝나는시간 고려
# 배수 모으기
fw = []
for i in range(n):
    times = c//freq[i]
    for j in range(1, times+1):
        fw.append(freq[i] * j)

# 중복 제거: set 사용
print(len(set(fw)))
'''


# *** 방법 2
# [0, 0, 0, ..., 0]
import sys

t = [0] * (c + 1)

for p in freq:
    # 주기가 1인 경우 모든 시간에 폭죽이 터지므로 즉시 종료
    if p == 1:
        print(c)
        sys.exit(0)
    
    # 배수 체크 (주기마다 터지는 시간 기록)
    for j in range(p, c + 1, p):
        t[j] = 1

# 폭죽이 터진 시간 개수 출력
print(sum(t))


'''
# 방법 3: 시간 초과
fireworks = set()

for f in freq:
    for t in range(f, c + 1, f):  # f의 배수만 추가
        fireworks.add(t)

print(len(fireworks))  # 중복 제거된 폭죽 시간 개수 출력
'''
