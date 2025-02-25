import sys


n = int(sys.stdin.readline().strip())
hlist = []
hlist = list(map(int, sys.stdin.readline().split()))

record = []
diff = 0
for i in range(n-1):
    if hlist[i] < hlist[i+1]:
        diff += hlist[i+1]-hlist[i]
    else:
        diff = 0
    record.append(diff)
        
print(max(record))
        
    

        

