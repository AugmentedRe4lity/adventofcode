with open('data') as f:
    d = f.read().split('\n')[:-1]

data = dict()


count = 0
for i in d:
    s = [j.split(' ') for j in i.split('contain')[1][1:].replace('.','').split(', ')]
    data[i.split('contain')[0][:-1].replace('bags','bag')] = [[j[0], ' '.join(j[1:]).replace('bags', 'bag')] for j in s]

bags = []

def f(b):
    for g in b:
        print(g)
        i = g[1]
        if not 'other' in i:
            j = int(g[0])
            for _ in range(j):
                f(data[i])
                bags.append(i)

f([['1', 'shiny gold bag']])

bags.remove('shiny gold bag')

print(len(bags))
