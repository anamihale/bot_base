import os


directory = '/Users/alenalapteva/Documents/Banks bot/database_ready'

files = os.listdir(directory)
files135_4 = filter(lambda x: x.endswith('_135_4.csv'), files)
norms = []
for filename in sorted(files135_4, key=lambda name: name[2:6]+ name[:2], reverse=True):
    if int(filename[2:6]) > 2010:
        with open('/Users/alenalapteva/Documents/Banks bot/database_ready' + '/' + filename, encoding='CP1251') as fin:
            fin.readline()
            for line in fin:
                line = line.split(sep=",")
                norms.append(line[:1]+line[2:])

files135_3 = filter(lambda x: x.endswith('2010_135_3.csv'), files)
for filename in sorted(files135_3, key=lambda name: name[2:6]+ name[:2], reverse=True):
    with open('/Users/alenalapteva/Documents/Banks bot/database_ready' + '/' + filename, encoding='CP1251') as fin:
        fin.readline()
        for line in fin:
            line = line.split(sep=",")
            norms.append(line[:1]+line[2:])

with open('Values.csv', 'w') as fout_norms:
    fout_norms.write("ID;Norm;Value;Date\n")
    for item in norms:
        print(*item, file=fout_norms, sep=';')

N = set()
for i in norms:
        if i[1] not in N:
            N.add(i[1])
print(N)