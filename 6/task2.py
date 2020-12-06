with open('data')as f:d=f.read()[:-1].split('\n\n')
s=0
for e in d:
    r=[1 if all([i in j for j in e.split('\n')])else 0 for i in e.split('\n')[0]]
    s+=sum(r)
print(s)
