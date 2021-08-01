from random import randint


amount_nums = int(input('Введите нужное количество чисел в массиве: '))
nums = [0] * amount_nums
for i in range(amount_nums):
    nums[i] = randint(-10, 10)
print('Массив: ', nums)
# сохранил отрицательные элементы в другом списке и нашел максимальное
nums_tmp = []
for idx in range(0, len(nums)):
    if nums[idx] < 0:
        nums_tmp.append(nums[idx])
max_num = max(nums_tmp)
# индексация в массиве начинается с 1
print(f'Максимальный отрицательный элемент: {max_num}, индекс: {nums.index(max_num) + 1}')
