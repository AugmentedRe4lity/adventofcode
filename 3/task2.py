

with open('data', 'r') as f:
    d = f.read().split('\n')[:-1]

r = 1

count = 0
i=0
for l in d:
    if l[i%len(l)]=='#':
        count+=1
    i+=1

r *= count

count = 0
i=0
for l in d:
    if l[i%len(l)]=='#':
        count+=1
    i+=3

r *= count

count = 0
i=0
for l in d:
    if l[i%len(l)]=='#':
        count+=1
    i+=5

r *= count

count = 0
i=0
for l in d:
    if l[i%len(l)]=='#':
        count+=1
    i+=7

r *= count

count = 0
i=0
for j, l in enumerate(d):
    if j%2==0:
        if l[i%len(l)]=='#':
            count+=1
        i+=1

r *= count

print(r)
