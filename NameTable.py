import os


directory = '/Users/alenalapteva/Documents/Banks bot/database_ready'

files = os.listdir(directory)
files135B = filter(lambda x: x.endswith('_135B.csv'), files)
ID_names = {}
synonyms = {}
for filename in sorted(files135B, key=lambda name: name[2:6]+name[:2], reverse=True):
    with open('/Users/alenalapteva/Documents/Banks bot/database_ready' + '/' + filename, encoding='CP1251') as fin:
        fin.readline()
        for line in fin:
            line = line.split(sep=",")
            name = line[7].replace('"""', '"')
            name = name.replace('""', '"')
            if line[0] not in ID_names:
                ID_names[line[0]] = name
            if name not in synonyms:
                synonyms[name] = line[0]


with open('Banks.csv', 'w') as fout_id:
    for key, value in ID_names.items():
        print(key, value, file=fout_id, sep=';')

with open('Synonyms.csv', 'w') as fout_syn:
    for key, value in synonyms.items():
        print(key, value, file=fout_syn, sep=';')

