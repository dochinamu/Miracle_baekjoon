import sys

# 이름을 거꾸로 바꾸는 함수
def reverse_name(name):
    reverse_name = ''
    for c in name:
        reverse_name = c + reverse_name
    return reverse_name

# 단어 개수 입력
n = int(sys.stdin.readline().strip())

# 단어 리스트 입력
words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip())

# 비밀번호 식별
for i in range(len(words)):
    if reverse_name(words[i]) in words:
        pw = words[i]
        # 길이, 중간 글자 출력
        print(len(pw), pw[len(pw)//2])
        break