from random import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    def merge(left_part, right_part, merged):

        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left_part) and right_cursor < len(right_part):

            if left_part[left_cursor] <= right_part[right_cursor]:
                merged[left_cursor + right_cursor] = left_part[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right_part[right_cursor]
                right_cursor += 1

        for left_cursor in range(left_cursor, len(left_part)):
            merged[left_cursor + right_cursor] = left_part[left_cursor]

        for right_cursor in range(right_cursor, len(right_part)):
            merged[left_cursor + right_cursor] = right_part[right_cursor]

        return merged

    return merge(left, right, arr)


if __name__ == '__main__':
    # одномерный вещественный массив, заданный случайными числами на промежутке [0; 50)
    nums = [round(random() * 50, 2) for num in range(10)]
    print(f'Неотсортированный список: {nums}')
    print(f'Отсортированный список:   {merge_sort(nums)}')
