while True:
    quantity = int(input('Введите количество элементов (n): '))
    if quantity <= 0:
        print('Количество элементов (n) должно быть больше нуля!')
    else:
        element, element_sum = 1, 0
        element_list = []
        for i in range(quantity):
            element_sum += element
            element_list.append(element)
            element /= -2
        print(f'Сумма из {quantity} элементов следующего ряда чисел: {element_list} равна {element_sum}')
        break
