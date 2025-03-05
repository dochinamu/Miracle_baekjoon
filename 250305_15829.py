import sys

def cha_to_int(cha):
    return ord(cha) - ord('a') + 1
    
def hash_func(str):
    sum = 0
    for i in range(len(str)):
        sum+=cha_to_int(str[i])*(pow(31, i))
        print(cha_to_int(str[i])*(pow(31, i)))
    return sum % 1234567891


l = int(sys.stdin.readline())

# .strip()을 통해 /n 개행 문자를 지워주어야 함
str = sys.stdin.readline().strip()

print(hash_func(str))