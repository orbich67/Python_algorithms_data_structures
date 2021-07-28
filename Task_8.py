quantity = int(input('Количество вводимых чисел: '))
number = int(input('Цифра, которую необходимо посчитать: '))
count = 0
for i in range(1, quantity + 1):
    num = int(input(f'Введите {i}-e число: '))
    while num > 0:
        if num % 10 == number:
            count += 1
        num = num // 10
print(f'Цифра {number} встречается {count} раз(а) в введенной последовательности чисел.')
