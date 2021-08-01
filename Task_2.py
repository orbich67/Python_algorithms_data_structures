from random import randint


amount_nums = int(input('Введите нужное количество чисел в массиве: '))
nums = [0] * amount_nums

even_nums = []
for i in range(amount_nums):
    nums[i] = randint(-100, 100)
    if nums[i] % 2 == 0:
        # индексация начинается с 1
        even_nums.append(i + 1)
print('Массив чисел: ', nums)
print('Индексы четных элементов: ', even_nums)
