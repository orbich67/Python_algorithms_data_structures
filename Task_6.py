from random import random


number = round(random() * 100)
try_number = 1
print("Отгадайте число от 0 до 100. У вас 10 попыток")
while try_number <= 10:
    user_number = int(input(f'{try_number}-я попытка: '))
    if user_number > number:
        print('Введенное число больше загаданного')
    elif user_number < number:
        print('Введенное число меньше загаданного')
    else:
        print(f'Вы угадали с {try_number}-й попытки число: {number}')
        break
    try_number += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано: ', number)
