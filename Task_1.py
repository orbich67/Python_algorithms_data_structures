import sys
from random import randint


# Lesson 3. Task 2. "Во втором массиве сохранить индексы четных элементов первого массива."
AMOUNT_NUMS = 1000000

# 1 вариант решения
nums = [0] * AMOUNT_NUMS
even_nums = []
for i in range(AMOUNT_NUMS):
    # для чистоты взял случайные числа с одним разрядом
    nums[i] = randint(0, 9)
    if nums[i] % 2 == 0:
        even_nums.append(i + 1)
print(f'Размер объекта {type(nums) =} (kB): {sys.getsizeof(nums) / 1024:.2f}')
print(f'Размер объекта {type(even_nums) = } (kB): {sys.getsizeof(even_nums) / 1024:.2f}')


# 2 вариант решения
# для чистоты взял случайные числа с одним разрядом
nums = (randint(0, 9) for num in range(AMOUNT_NUMS))
print(f'\nРазмер объекта {type(nums) =} (kB): {sys.getsizeof(nums) / 1024:.2f}')

even_nums = []
for idx, num in enumerate(nums):
    if num % 2 == 0:
        even_nums.append(idx + 1)
# размер в памяти до перевода в кортеж
print(f'Размер объекта {type(even_nums) = } (kB): {sys.getsizeof(even_nums) / 1024:.2f}')
even_nums = tuple(even_nums)
print(f'Размер объекта {type(even_nums) = } (kB): {sys.getsizeof(even_nums) / 1024:.2f}')

# Вывод: кортеж занимает чуть меньше места в памяти, чем список. Генератор занимает в памяти
# всегда постоянную величину не зависимо от количества элементов (112 байт). Плюсы использования
# генератора - не занимает места в памяти, минусы - одноразовый(истощается по мере обращения к элементам).

# Пример работы кода:
# Размер объекта type(nums) =<class 'list'> (kB): 7812.55
# Размер объекта type(even_nums) = <class 'list'> (kB): 4189.46
#
# Размер объекта type(nums) =<class 'generator'> (kB): 0.11
# Размер объекта type(even_nums) = <class 'list'> (kB): 4189.46
# Размер объекта type(even_nums) = <class 'tuple'> (kB): 3905.55

# Версия Python 3.8, Windows 10 Pro, ver. 20H2, 64-разрядная операционная система.
