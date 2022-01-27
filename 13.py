Sum = 0
print ('Введите количество билетов')
L = int(input()) 
for i in range(L):
    print ('Введите возраст участника')
    age = int(input())
    if age < 18:
        print ('Билет бесплатный')
    if age >= 18 and age < 25:
        print ('Билет стоит 990 руб')
        Sum += 990
    if age >= 25:
        print ('Билет стоит 1390 руб')
        Sum += 1390
if L > 3 :
    print ('Итоговая сумма составила (*Скидка за количество участников 10%)', Sum*0.9)
else :
    print ('Итоговая сумма составила ', Sum)
