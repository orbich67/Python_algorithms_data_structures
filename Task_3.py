# 1 вариант решения
number = int(input('Введите число: '))
number = str(number)
print(int(number[::-1]))

# 2 вариант решения
number = int(input('Введите число: '))
number = str(number)
number_revers = []
for i in range(len(number)):
    number_revers.insert(0, number[i])
print(int(''.join(number_revers)))
