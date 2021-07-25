a = int(input('Введите три 1-е число: '))
b = int(input('Введите три 2-е число: '))
c = int(input('Введите три 3-е число: '))
if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)
