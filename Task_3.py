from random import randint


amount_nums = int(input('Введите нужное количество чисел в массиве: '))
nums = [0] * amount_nums

for idx in range(amount_nums):
    nums[idx] = randint(-100, 100)
min_num, max_num = min(nums), max(nums)
idx_min, idx_max = nums.index(min_num), nums.index(max_num)

# индексация в массиве начинается с 1
print(f'{nums}, \nИндекс min: {idx_min + 1}; Индекс max: {idx_max + 1}')
nums[idx_min], nums[idx_max] = nums[idx_max], nums[idx_min]
min_num, max_num = min(nums), max(nums)
idx_min, idx_max = nums.index(min_num), nums.index(max_num)
print(f'{nums}, \nИндекс min: {idx_min + 1}; Индекс max: {idx_max + 1}')
