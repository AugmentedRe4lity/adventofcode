

with open('data', 'r') as f:
    d = f.read().split('\n')[:-1]

count = 0
i=0
for l in d:
    if l[i%len(l)]=='#':
        count+=1
    i+=3

print(count)
