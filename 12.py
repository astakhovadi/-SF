per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = 100000

for i in range (4):
    print('deposit in ', (list(per_cent.keys())[i]), ': ', money*(list(per_cent.values())[i])/100)

print('Максимальная сумма, которую вы можете заработать = ',money/100*max(list(per_cent.values())))
