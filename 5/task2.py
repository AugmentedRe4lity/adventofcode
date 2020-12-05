

with open('data') as f:
    d = f.read().split('\n')[:-1]

id = []

for l in d:
    r = l[:7]
    c = l[7:]
    nr = ''.join(['0' if i.upper()=='F' else '1' for i in r])
    r = int(nr, 2)
    nc = ''.join(['0' if i.upper()=='L' else '1' for i in c])
    c = int(nc, 2)
    id.append(8*r+c)
    id.sort()


for i in range(len(id))[:-1]:
    if id[i]+1!=id[i+1]:
        print(id[i]+1)
