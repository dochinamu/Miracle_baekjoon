import sys


n = int(sys.stdin.readline())

scores = []
scores = list(map(int, sys.stdin.readline().split()))

max_score = max(scores)
min_score = min(scores)

print(max_score - min_score)