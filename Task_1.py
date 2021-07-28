print('Введите ноль в "Действие" для выхода из программы.')
while True:
    num1, num2, sign = float(input('Число 1: ')), float(input('Число 2: ')), input("Действие (+, -, *, /, 0): ")
    if sign == '0':
        break
    if sign in ('+', '-', '*', '/'):
        if sign == '+':
            print(f'{num1} {sign} {num2} = {num1 + num2}')
        elif sign == '-':
            print(f'{num1} {sign} {num2} = {num1 - num2}')
        elif sign == '*':
            print(f'{num1} {sign} {num2} = {num1 * num2}')
        elif sign == '/':
            if num2 != 0:
                print(f'{num1} {sign} {num2} = {num1 / num2}')
            else:
                print('Делить на ноль нельзя!')
    else:
        print('Нет такой операции!')
