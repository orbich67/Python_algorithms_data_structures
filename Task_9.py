number = int(input('Введите натуральное число: '))
max_sum = 0
max_num = 0
while number != 0:
    num = number
    num_sum = 0
    while number > 0:
        num_sum += number % 10
        number //= 10
    if num_sum > max_sum:
        max_sum = num_sum
        max_num = num
    number = int(input('Введите следующее натуральные число (0 - расчет): '))
print('Число', max_num, 'имеет максимальную сумму цифр:', max_sum)
