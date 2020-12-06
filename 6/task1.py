

with open('data') as f:
    d = f.read()[:-1].split('\n\n')
sum = 0

for e in d:
    es = []
    r = [i for i in e.split('\n')[0]]
    for i in e.split('\n'):
        for c in i:
            if not c in r:
                r.append(c)
    sum+=len(r)

print(sum)
