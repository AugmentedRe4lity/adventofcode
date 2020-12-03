

with open('data', 'r') as f:
    d = [int(i.strip()) for i in f.read().split('\n')[:-1]]

for i in d:
    for j in d:
        for b in d:
            if i+j+b==2020:
                print(f'{i+j+b}\t{i*j*b}')
