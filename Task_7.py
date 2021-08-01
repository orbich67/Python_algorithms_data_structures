from random import randint


amount_nums = int(input('Введите нужное количество чисел в массиве: '))
nums = [0] * amount_nums
for i in range(amount_nums):
    nums[i] = randint(0, 100)
# скопировал массив, чтобы не изменять оригинал
nums_tmp = nums.copy()
min1 = min(nums_tmp)
nums_tmp.remove(min1)
min2 = min(nums_tmp)
del nums_tmp
print(f'Массив: {nums} \nНаименьшие элементы массива: {min1}, {min2}')
