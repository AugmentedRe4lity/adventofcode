

with open('data') as f:
    d = f.read().split('\n')[:-1]

mid = 0

for l in d:
    r = l[:7]
    c = l[7:]
    nr = ''.join(['0' if i.upper()=='F' else '1' for i in r])
    r = int(nr, 2)
    nc = ''.join(['0' if i.upper()=='L' else '1' for i in c])
    c = int(nc, 2)
    id = 8*r+c
    mid = max(mid, id)
print(mid)
