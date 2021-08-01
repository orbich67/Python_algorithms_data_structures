from random import randint


amount_nums = int(input('Введите нужное количество чисел в массиве: '))
nums = [0] * amount_nums
for i in range(amount_nums):
    nums[i] = randint(0, 10)
print('Массив: ', nums)
num = nums[0]
max_repeat = 1
for i in range(amount_nums - 1):
    repeat = 1
    for j in range(i + 1, amount_nums):
        if nums[i] == nums[j]:
            repeat += 1
    if repeat > max_repeat:
        max_repeat = repeat
        num = nums[i]
if max_repeat > 1:
    print(f'Число "{num}" встречается "{max_repeat}" раз(а)')
else:
    print('В массиве нет повторяющихся чисел')
