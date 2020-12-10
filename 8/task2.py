with open('data') as f:
    d = f.read().split('\n')[:-1]

bd = []

for i, j in enumerate(d):
    if 'nop' in j:
        j = j.replace('nop', 'jmp')
        bd.append(d[:i]+[j]+d[i+1:])
    if 'jmp' in j:
        j = j.replace('jmp', 'nop')
        bd.append(d[:i]+[j]+d[i+1:])

for d in bd:
    i = 0
    acc = 0

    cl = []

    for _ in d:
        cl.append(0)
    t = True
    while i<len(d):
        for j, l in enumerate(d[i:]):
            if any([a>1 for a in cl]):
                i = len(d)
                t = False
                break
            j = j+i
            cl[j]+=1
            cmd, add = l.split()[0], int(l.split()[1])
            if cmd == 'nop':
                pass
            elif cmd == 'acc':
                if any([a>1 for a in cl]):
                    i = len(d)
                    t = False
                    break
                acc += add
            elif cmd == 'jmp':
                i = j+add
                break
    if t:
        print(acc)
