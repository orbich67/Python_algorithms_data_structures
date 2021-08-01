matrix = []
for line in range(4):
    string = []
    sum_num = 0
    print(f'{line + 1}-я строка матрицы.')
    for el in range(4):
        num = int(input(f'{el + 1}-й элемент: '))
        sum_num += num
        string.append(num)
    string.append(sum_num)
    matrix.append(string)

print()
for line in matrix:
    for num in line:
        print(num, end='\t')
    print()
