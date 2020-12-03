

with open('data', 'r') as f:
    d = f.read().split('\n')[:-1]

count = 0

for e in d:
    min = int(e[:e.find('-')])
    max = int(e[e.find('-')+1:e.find(' ')])
    char = e[e.find(' ')+1:e.find(':')]
    passwd = e[e.find(': ')+2:]
    i = passwd.count(char)
    if i>=min and i<=max:
        count += 1

print(count)
