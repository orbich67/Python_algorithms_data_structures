number = int(input('Введите номер буквы в алфавите: '))
if 0 < number <= 26:
    value = ord('a') + number - 1
    print('Это буква', chr(value))
else:
    print('Нет буквы с таким номером!')
