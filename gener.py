print('stop = выход.\nскип = пропустить.\nдальше изи = выбрать другой раздел и завершить текущий.')
from random import choice
with open('words.txt') as text:
    data, name = [], []
    for t in text:
        if t[0] == '#':
            data.append([t.strip()])
            name.append(t.strip())
        else:
            data[-1].append(t.strip())
    data = {x[0]:x[1:] for x in data}
    com = ''
    while 'stop' not in com:
        print('Выбери: ')
        for i in range(len(name)): print(i + 1, '->', name[i][1:])
        tmp = int(input()) - 1
        kop = data[name[tmp]]
        if name[tmp] != '#Ударения': kop = [i.lower() for i in kop]
        while kop:
            lkm = choice(kop)
            if name[tmp] == '#Ударения': print(lkm.lower(), ' '*11, len(kop))
            elif name[tmp] == '#ННН': print(lkm.replace('нн', '_').replace('н', '_'), ' '*11, len(kop))
            else: print(*[[i, '_'][i in 'уеоаияюэы'] for i in lkm], ' '*13, len(kop), sep='')
            com = input().strip()
            if 'скип' in com:
                kop.remove(lkm)
                continue
            if com in lkm.split(): kop.remove(lkm)
            elif 'stop' in com or 'дальше изи' in com: break
            else:
                while com not in lkm.split() and 'stop' not in com and \
                  'скип' not in com and 'дальше изи' not in com:
                    print(lkm)
                    com = input().strip()
            if 'stop' in com or 'дальше изи' in com: break
            if 'скип' in com:
                kop.remove(lkm)
                continue

