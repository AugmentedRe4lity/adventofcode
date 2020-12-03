

with open('data', 'r') as f:
    d = f.read().split('\n')[:-1]

count = 0

for e in d:
    min = int(e[:e.find('-')])
    max = int(e[e.find('-')+1:e.find(' ')])
    char = e[e.find(' ')+1:e.find(':')]
    passwd = e[e.find(': ')+2:]
    i = passwd.count(char)
    if passwd[min-1]==char and passwd[max-1]==char:
        pass
    elif passwd[min-1]==char or passwd[max-1]==char:
        count+=1

print(count)
