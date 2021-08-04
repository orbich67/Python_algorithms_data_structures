import cProfile


# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# для простоты использовал словарь


# 1 вариант алгоритма
def div_count_1(number):
    amount_nums = dict()
    for divisor in range(2, 9 + 1):
        amount_nums[divisor] = number // divisor
    return amount_nums

# py -m timeit -n 100 -s "import Task_1" "Task_1.div_count_1(99)"
# "import Task_1" "Task_1.div_count_1(99)"
# 100 loops, best of 5: 1.04 usec per loop
# "import Task_1" "Task_1.div_count_1(999)"
# 100 loops, best of 5: 1.08 usec per loop
# "import Task_1" "Task_1.div_count_1(9999)"
# 100 loops, best of 5: 1.12 usec per loop
# "import Task_1" "Task_1.div_count_1(99999)"
# Алгоритм работает приблизительно за O(1), т.к. при увеличении количества элементов в 10 раз на каждый запуск
# время выполнения увеличивалось незначительно.
# Самый быстрый алгоритм.


# 2 вариант алгоритма
def div_count_2(number):
    amount_nums = dict()
    for divisor in range(2, 9 + 1):
        amount_nums[divisor] = 0
        for num in range(2, number + 1):
            if num % divisor == 0:
                amount_nums[divisor] += 1
    return amount_nums

# py -m timeit -n 100 -s "import Task_1" "Task_1.div_count_2(99)"
# "import Task_1" "Task_1.div_count_2(99)"
# 100 loops, best of 5: 47.8 usec per loop
# "import Task_1" "Task_1.div_count_2(999)"
# 100 loops, best of 5: 518 usec per loop
# "import Task_1" "Task_1.div_count_2(9999)"
# 100 loops, best of 5: 5.48 msec per loop
# "import Task_1" "Task_1.div_count_2(99999)"
# 100 loops, best of 5: 55.2 msec per loop
# Алгоритм работает приблизительно за O(n), т.к. при увеличении количества элементов в 10 раз на каждый запуск
# время выполнения увеличивается приблизительно в 10 раз.


# 3 вариант алгоритма
def div_count_3(number):
    amount_nums = dict()
    nums = [number // divisor for divisor in range(2, 9 + 1)]
    for num in range(2, 9 + 1):
        amount_nums[num] = nums[num - 2]
    return amount_nums

# "import Task_1" "Task_1.div_count_3(99)"
# 100 loops, best of 5: 1.91 usec per loop
# "import Task_1" "Task_1.div_count_3(999)"
# 100 loops, best of 5: 1.96 usec per loop
# "import Task_1" "Task_1.div_count_3(9999)"
# 100 loops, best of 5: 1.98 usec per loop
# "import Task_1" "Task_1.div_count_3(99999)"
# 100 loops, best of 5: 2.07 usec per loop
# Алгоритм работает приблизительно за O(1), т.к. при увеличении количества элементов в 10 раз на каждый запуск
# время выполнения увеличивалось незначительно.


if __name__ == '__main__':
    print(cProfile.run('div_count_1(99999)'))
    # 1    0.000    0.000    0.000    0.000 Task_1.py:10(div_count_1)
    print(cProfile.run('div_count_2(99999)'))
    # 1    0.058    0.058    0.058    0.058 Task_1.py:29(div_count_2)
    print(cProfile.run('div_count_3(99999)'))
    # 1    0.000    0.000    0.000    0.000 Task_1.py:52(div_count_3)
    print(div_count_1(99))
    print(div_count_2(99))
    print(div_count_3(99))
# Вывод: алгоритм div_count_1 самый быстрый по скорости.
