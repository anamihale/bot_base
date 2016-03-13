import os
from datetime import datetime, date, timedelta

def get_status(bank_id):
    def is_violation(norms, value):
        violations = {'total': 0}
        for norm in norms:
            violations[norm[1]] = 0
        for n in norms:
            n_date = n[0].split(sep='/')
            n_date = date(int(n_date[2]), int(n_date[0]), int(n_date[1]))
            for val in value:
                if n[1] == val[0] and n_date >= val[2]:
                    if n[3] == 'max' and float(val[1]) > float(n[2]) or n[3]  == 'min' and float(val[1]) < float(n[2]):
                        violations['total'] += 1
                        violations[n[1]] += 1
        return violations

    norms = [['01/01/2001', 'Н1.0', '10', 'min'], ['01/01/2001', 'Н1.1', '5', 'min'], ['01/01/2001', 'Н1.2', '5.5', 'min'], ['01/01/2001', 'Н2', '15', 'min'], ['01/01/2001', 'Н3', '50', 'min'], ['01/01/2001', 'Н4', '120', 'max'], ['01/01/2001', 'Н6', '25', 'max'], ['01/01/2001', 'Н7', '800', 'max'], ['01/01/2001', 'Н9.1', '50', 'max'], ['01/01/2001', 'Н10.1', '3', 'max'], ['01/01/2001', 'Н12', '25', 'max'], ['01/01/2001', 'Н15', '100', 'min'], ['01/01/2001', 'Н16', '100', 'max'], ['01/01/2001', 'Н16.1', '0', 'max'], ['01/01/2001', 'Н18', '100', 'min'], ['01/01/2015', 'Н1.2', '6', 'min'], ['01/01/2016', 'Н1.0', '8', 'min'], ['01/01/2016', 'Н1.1', '4.5', 'min']]

    # убрать
    bank_id = '2999'
    vals = set()
    with open("Values.csv") as fin:
        fin.readline()
        for line in fin:
            line.rstrip()
            line = line.split(sep=";")
            if line[0] == bank_id:
                v_date = line[3].split(sep='/')
                v_date = date(int(v_date[2]), int(v_date[0]), int(v_date[1]))
                vals.add((line[1], line[2], v_date))

    l_vals = sorted(vals, key=lambda x: x[2], reverse=True)
    final_date = l_vals[0][2]

    count = 0
    while count < len(l_vals) and l_vals[count][2] > final_date - timedelta(days=182):
        count += 1
    l_vals = l_vals[:count]
    violations = is_violation(norms, l_vals)

    if violations['total'] == 0:
        half_year = "У банка за за полгода до %s наружений не было" %final_date
    else:
        half_year = "Всего за полгода до %s у банка было %d нарушений. Из них нарушены: \n" %(final_date, violations['total'])
        for key, value in violations.items():
            if key != 'total' and value != 0:
                half_year += "норматив %s - %d раз \n" %(key, value)

    count_m = 0
    while count_m < len(l_vals) and l_vals[count_m][2] > final_date - timedelta(days=30):
        count_m += 1
    l_vals = l_vals[:count_m]
    violations_m = is_violation(norms, l_vals)

    if violations_m['total'] == 0:
        month = "У банка за за месяц до %s наружений не было" %final_date
    else:
        month = "Всего за месяц до %s у банка было %d нарушений. Из них нарушены:\n" %(final_date, violations_m['total'])
        for key, value in violations_m.items():
            if key != 'total' and value != 0:
                month += "норматив %s - %d раз \n" %(key, value)

    if violations_m['total'] == 0 and violations['total']-violations_m['total'] == 0:
        signal = "Зеленый сигнал. Опасности нет.\n"
    elif violations_m['total'] == 0 and violations['total']-violations_m['total'] != 0:
        signal = "Желтый сигнал опасности. У банка недавно были нарушения.\n"
    elif violations_m['total'] != 0 and violations['total']-violations_m['total'] == 0:
        signal = "Оранжевый сигнал опасности. У банка появились нарушения.\n"
    elif violations_m['total'] != 0 and violations['total']-violations_m['total'] != 0:
        signal = "Красный сигнал опасности. Нарушения существуют длительное время.\n"

    return (signal, month, half_year)

print(get_status('2999'))