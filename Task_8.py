year = int(input('Введите год для проверки: '))
if year % 4 != 0:
    print("Год обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный')
    else:
        print('Год обычный')
else:
    print('Год високосный')
