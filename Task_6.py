from random import randint


amount_nums = int(input('Введите нужное количество чисел в массиве: '))
nums = [0] * amount_nums
for i in range(amount_nums):
    nums[i] = randint(-100, 100)
print('Массив: ', nums)

min_num, max_num = min(nums), max(nums)
min_idx, max_idx = nums.index(min_num), nums.index(max_num)
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
sum_nums = 0

for idx in range(min_idx + 1, max_idx):
    sum_nums += nums[idx]
if sum_nums != 0:
    print(f'Сумма элементов между min "{min_num}" и max "{max_num}": {sum_nums}')
else:
    print('Нет значений между максимальным и минимальным элементом.')
