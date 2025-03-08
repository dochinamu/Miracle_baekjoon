import sys

def recursion(s, l, r):
    if l >= r:
        if len(s)//2+1 > l:
            times = l
        else:
            times = len(s)//2 +1
        return 1, times
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)
    
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(sys.stdin.readline())

slist = []
for i in range(t):
    slist.append(sys.stdin.readline().strip())

    flag = isPalindrome(slist[i])[0]
    times = isPalindrome(slist[i])[1]
    print(flag, times)

