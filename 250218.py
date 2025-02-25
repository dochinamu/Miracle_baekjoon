
# input
str = input('')

# Split by space
str_list = str.split(" ")

num1 = int(str_list[0])
num2 = int(str_list[1])


# 방법1: 가능한 범위 내 모든 수가 공배수인지 확인
'''
for i in range(max(num1, num2), num1*num2+1):
    # 오답: if ((num1 % i == 0) and (num2 % i == 0)):
    if ((i % num1 == 0) and (i % num2 == 0)):
        print(i)
        break
'''

# 방법2: 유클리드 호재법 - 최대공약수 + 최소공배수
def Euclidean(a, b):
    start = a*b
    # 나누는 수가 0이 될 때까지 나머지로 바꿔준다
    while b != 0:
        r = a % b 
        a = b
        b = r
        # 두 수의 곱을 최대공약수로 나눈 값이 최소공배수 
    return start // a

print(Euclidean(num1, num2))