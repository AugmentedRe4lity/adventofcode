with open('data')as f:print(sum([sum([1 if all([i in j for j in e.split('\n')])else 0 for i in e.split('\n')[0]])for e in f.read()[:-1].split('\n\n')]))
