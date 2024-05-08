a = int(input())
b = input()
if b == 'январь':
    a = a+0
elif b == 'февраль':
    a = a+31

list_ = []
with open('holiday.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        list_.append(line)

print(list_[a])