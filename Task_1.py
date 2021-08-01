amount_nums = [0] * 8
for num in range(2, 99 + 1):
    for divisor in range(2, 9 + 1):
        if num % divisor == 0:
            amount_nums[divisor - 2] += 1
for idx in range(0, 8 + 1):
    if idx < len(amount_nums):
        print(f'Чисел кратных {idx + 2} - {amount_nums[idx]}')
