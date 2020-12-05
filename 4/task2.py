count = 0

criteria = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
hd = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']

inp = dict()

with open('data', 'r') as f:
    d = f.read().split('\n\n')


def valid(inp):

    for k, v in inp.items():
        inp[k] = v.split(' ')[0]

    if inp['byr'].isdigit() and len(inp['byr'])==4:
        byr = int(inp['byr'])
    else:
        return False
    if inp['iyr'].isdigit() and len(inp['iyr'])==4:
        iyr = int(inp['iyr'])
    else:
        return False
    if inp['eyr'].isdigit() and len(inp['eyr'])==4:
        eyr = int(inp['eyr'])
    else:
        return False
    if inp['hgt'][-2:] == 'cm':
        if int(inp['hgt'][:-2])<150 or int(inp['hgt'][:-2])>193:
            return False
    elif inp['hgt'][-2:] == 'in':
        if int(inp['hgt'][:-2])<59 or int(inp['hgt'][:-2])>76:
            return False
    else:
        return False
    hcl = inp['hcl']
    ecl = inp['ecl']
    pid = inp['pid']

    if byr>2002 or byr<1920:
        return False
    if iyr>2020 or iyr<2010:
        return False
    if eyr>2030 or eyr<2020:
        return False
    if not hcl.startswith('#') or not all([i.lower() in hd for i in hcl[1:]]):
        return False

    if not ecl in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False
    if not pid.isdigit() or not len(pid)==9:
        return False

    return True


for e in d:
    inp = dict()
    for i in criteria:
        if i in e:
            inp[i[:-1]] = e[e.find(i)+4:]
            inp[i[:-1]] = inp[i[:-1]][:min(inp[i[:-1]].find(' ') if inp[i[:-1]].find(' ')!=-1 else 10, inp[i[:-1]].find('\n') if inp[i[:-1]].find('\n')!=-1 else 10)]
    if(all([i in inp.keys() for i in [j[:-1] for j in criteria]])):
        if valid(inp):
            count+=1



print(count)
