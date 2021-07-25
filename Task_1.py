number = int(input('Введите трехзначное число: '))
result = number % 10 + number % 100 // 10 + number // 100
print('Сумма чисел равна: ', result)
