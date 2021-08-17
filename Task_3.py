from random import random


def median_arr(arr):
    for i in arr:
        idx = 0
        for j in arr:
            if i < j:
                idx += 1
        if len(arr) == 2 * idx + 1:

            return i


if __name__ == '__main__':
    m = 2
    size = 2 * m + 1
    nums = [round(random() * 50, 2) for num in range(size)]
    print(f'Неотсортированный список: {nums}\nМедиана: {median_arr(nums)}')
    print(f'Отсортированный список:   {sorted(nums)}')
