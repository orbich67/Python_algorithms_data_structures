import cProfile


def not_eratosthenes(number):
    nums = []
    for number in range(0, number + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                nums.append(number)
    return nums

# "import Task_2" "Task_2.not_eratosthenes(10)"
# 100 loops, best of 5: 3.61 usec per loop
# "import Task_2" "Task_2.not_eratosthenes(100)"
# 100 loops, best of 5: 73.2 usec per loop
# "import Task_2" "Task_2.not_eratosthenes(1000)"
# 100 loops, best of 5: 3.9 msec per loop
# Алгоритм работает приблизительно за O(2*n), т.к. при увеличении количества элементов в 10 раз на каждый запуск
# время выполнения увеличивается приблизительно в 20 раз.


def eratosthenes(number):
    nums = []
    sieve = set(range(2, number + 1))
    while sieve:
        prime = min(sieve)
        nums.append(prime)
        sieve -= set(range(prime, number + 1, prime))
    return nums

# "import Task_2" "Task_2.eratosthenes(10)"
# 100 loops, best of 5: 3.79 usec per loop
# "import Task_2" "Task_2.eratosthenes(100)"
# 100 loops, best of 5: 39.3 usec per loop
# "import Task_2" "Task_2.eratosthenes(1000)"
# 100 loops, best of 5: 759 usec per loop
# Алгоритм работает приблизительно за O(n), т.к. при увеличении количества элементов в 10 раз на каждый запуск
# время выполнения увеличивается приблизительно в 10 раз.


if __name__ == '__main__':
    print(cProfile.run('not_eratosthenes(9000)'))
    # 1    0.268    0.268    0.268    0.268 Task_2.py:4(not_eratosthenes)
    print(cProfile.run('eratosthenes(9000)'))
    # 1    0.003    0.003    0.029    0.029 Task_2.py:23(eratosthenes)
    print(not_eratosthenes(100))
    print(eratosthenes(100))
# Вывод: алгоритм eratosthenes быстрее, чем алгоритм not_eratosthenes
