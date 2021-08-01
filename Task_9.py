from random import randint


column = int(input('Количество столбцов в матрице: '))
line = int(input('Количество строк в матрице: '))
num_min, num_max = int(input('Числа в матрице от: ')), int(input('Числа в матрице до: '))
matrix = []
for i in range(line):
    string = []
    for j in range(column):
        num = randint(num_min, num_max)
        string.append(num)
    matrix.append(string)

el_max = num_min - 1
for j in range(column):
    el_min = num_max + 1
    for i in range(line):
        if matrix[i][j] < el_min:
            el_min = matrix[i][j]
    if el_min > el_max:
        el_max = el_min

print()
for line in matrix:
    for num in line:
        print(num, end='\t')
    print()
print(f'\nМаксимальный элемент среди минимальных в столбцах матрицы: "{el_max}"')
