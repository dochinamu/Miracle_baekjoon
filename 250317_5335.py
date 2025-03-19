# format()

import sys
import math

# TC Num 입력
t = int(sys.stdin.readline())

# 연산식 입력
op = []
for i in range(t):
    op.append(sys.stdin.readline().split())
    for j in range(1, len(op[i])):
        # 연산 처리
        if op[i][j] == "@":
            op[i][0] = float(op[i][0])*3
        elif op[i][j] == "%":
            op[i][0] = float(op[i][0])+5
        elif op[i][j] == "#":
            op[i][0] = float(op[i][0])-7
    # 소수점 둘째자리까지 표기
    print("{:.2f}".format(op[i][0]))



