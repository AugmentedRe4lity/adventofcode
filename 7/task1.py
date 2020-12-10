with open('data') as f:
    d = f.read().split('\n')[:-1]

data = dict()


count = 0
for i in d:
    s = [j.split(' ') for j in i.split('contain')[1][1:].replace('.','').split(', ')]
    data[i.split('contain')[0][:-1].replace('bags','bag')] = [' '.join(j[1:]).replace('bags', 'bag') for j in s]

for k, v in data.items():
    l = v
    print(l)
    nl = []
    r = True
    c = False
    while r:
        nl = []
        if len(l)==0:
            r=False
            break
        for i in l:
            print(l)
            if i == 'shiny gold bag':
                c = True
            elif 'other' in i:
                pass
            else:
                print(2, i)
                for j in data[i]:nl.append(j)

        if all(['other' in i for i in l]):
            break
        l = nl
    if c:
        count+=1
print(count)
