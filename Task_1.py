from random import randint


def bubble_sort(arr):
	n, replacement = 1, 0
	while n < len(arr):
		for idx in range(len(arr) - n):
			if arr[idx] < arr[idx + 1]:
				arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
				replacement = 1
		n += 1
		if replacement == 0:
			# выход из цикла, если нет замен
			break
	return arr


if __name__ == '__main__':
	# одномерный целочисленный массив случайных чисел на промежутке [-100; 100)
	nums = [randint(-100, 99) for num in range(10)]
	print(f'Неотсортированный список: {nums}')
	print(f'Отсортированный список:   {bubble_sort(nums)}')
