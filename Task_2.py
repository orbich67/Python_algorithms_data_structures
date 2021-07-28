number = int(input('Введите натуральное число: '))
number = str(number)
even_nums, odd_nums = [], []
for i in range(len(number)):
    if int(number[i]) % 2 == 0:
        even_nums.append(number[i])
    else:
        odd_nums.append(number[i])
even, odd = len(even_nums), len(odd_nums)
even_nums, odd_nums = ', '.join(even_nums), ', '.join(odd_nums)
print(f'В числе {number}: {even} четные цифры ({even_nums}) и {odd} нечетные ({odd_nums})')
