import sys

# count(), sorted(), <

def reg(n1, n2):
    l=n1.count('L')+n2.count('L')
    o=n1.count('O')+n2.count('O')
    v=n1.count('V')+n2.count('V')
    e=n1.count('E')+n2.count('E')
    
    return ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)) % 100
    
e_name = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

team_name = []
for _ in range (n):
    team_name.append(sys.stdin.readline().strip())

value = []
max_index = []
for i in team_name:
    value.append(reg(e_name, i))
    
for i in range(len(value)):
    if value[i] == max(value):
        max_index.append(i)

if len(max_index) >= 2:
    max_list = []
    for i in max_index:
        max_list.append(team_name[i])
    print(sorted(max_list)[0])
else:
    print(team_name[max_index[0]])
