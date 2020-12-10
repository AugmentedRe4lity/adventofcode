with open('data') as f:
    d = f.read().split('\n')[:-1]

i = 0
acc = 0

cl = []

for _ in d:
    cl.append(0)

while i!=len(d)-1:
    for j, l in enumerate(d[i:]):
        if any([a>1 for a in cl]):
            print(acc)
            exit()
        j = j+i
        cl[j]+=1
        cmd, add = l.split()[0], int(l.split()[1])
        if cmd == 'nop':
            pass
        elif cmd == 'acc':
            print(add)
            if any([a>1 for a in cl]):
                print(acc)
                exit()
            acc += add
        elif cmd == 'jmp':
            i = j+add
            break
