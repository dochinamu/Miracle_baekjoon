import sys

# 입력
n_list = []
for i in range(10):
    n_list.append(int(sys.stdin.readline()))

# 연산
print(sum(n_list) // 10)

# max(iterable, *, default, key=None) 
# 공식 문서 https://docs.python.org/ko/3/library/functions.html#max
# 블로그 (key) https://think-tech.tistory.com/13
# 블로그 (여러 개 자료 비교) https://m.blog.naver.com/jkg57/222110464419
#  key 함수가 반환하는 값이 비교 기준, 반환되는 건 원소 그 자체

print(max(n_list, key = n_list.count))