count = 0

criteria = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

with open('data', 'r') as f:
    d = f.read().split('\n\n')

for e in d:
    c = 0
    for i in criteria:
        if i in e:
            c +=1
    if c==len(criteria):
        count += 1

print(count)
