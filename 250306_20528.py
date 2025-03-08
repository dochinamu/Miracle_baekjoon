import sys

n = int(sys.stdin.readline())

str = []
str = sys.stdin.readline().split()

first = str[0][0]
bool = True
for i in str:
    if first != i[0]:
        bool = False
        break

if bool == True:
    print(1)
else:
    print(0)