import sys

words = [sys.stdin.readline().strip() for _ in range(5)]

max_len=0
for word in words:
    max_len = max(max_len, len(word))
    
for i in range(max_len):
    for j in range(5):
        if i >= len(words[j]):
            continue
        else:
            print(words[j][i], end='')


    