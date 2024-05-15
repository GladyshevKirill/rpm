a = int(input('Введите день от 1 до 31: '))
b = int(input('Введите месяц от 1 до 12 : '))
if b > 12:
    print ('Ошибка! В году 12 месяцев!!!')
else: 
    pass
if (b == 4 or b == 6 or b == 9 or b == 11) and a> 30:
    print ('Ошибка! В месяце 30 дней')
elif (b == 2) and a > 28:
    print ('Ошибка! В феврале 28 дней ')
elif (b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12) and a>31:
    print ('Ошибка! В месяце 31 день')
elif (a<=0):
    print ('Ошибка! Неверное число')
else:
    m1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    C = m1[b-1] + a

list_ = []
with open('holiday.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        list_.append(line)

print(list_[C])