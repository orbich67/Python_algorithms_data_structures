while True:
    number = int(input('Введите любое натуральное число: '))
    if number < 0:
        print('Отрицательные и нецелые числа к натуральным не относят!')
    else:
        sum_left = 0
        for i in range(1, number + 1):
            sum_left += i
        sum_right = number * (number + 1) // 2
        if sum_left != sum_right:
            print(f'{sum_left} ≠ {sum_right} выражение не верно!')
            break
        print(f'{sum_left} = {sum_right} выражение верно!')
        break
