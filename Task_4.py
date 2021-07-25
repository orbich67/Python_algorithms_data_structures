import random


a, b = int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: '))
print('Случайное целое число: ', random.randint(a, b))
a, b = int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: '))
print('Случайное вещественное число: ', random.random() * (b - a) + a)
symbols = input('Введите случайные символы: ')
print('Случайный символ: ', random.choice(symbols))
