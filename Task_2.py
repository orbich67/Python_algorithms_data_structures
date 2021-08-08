def transfer_hex_dec(num):
    """ Переводит шестнадцатеричное число в десятеричное """
    data = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}
    num_dec = 0
    for idx, el in enumerate(num[::-1]):
        num_dec += 16 ** idx * data.get(el)
    return num_dec


def transfer_dec_hex(num):
    """ Переводит десятеричное число в шестнадцатеричное """
    data = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
            6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
            12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    num_hex = []
    while num > 0:
        if num // 16 == 0:
            num_hex.append(data.get(num % 16))
            num_hex.reverse()
            break
        else:
            num_hex.append(data.get(num % 16))
            num = num // 16
    return num_hex


def sum_hex(a, b):
    result = transfer_hex_dec(a) + transfer_hex_dec(b)
    return transfer_dec_hex(result)


def multiply_hex(a, b):
    result = transfer_hex_dec(a) * transfer_hex_dec(b)
    return transfer_dec_hex(result)


def num_list(num):
    """ Переводит строку в список """
    return [num[idx] for idx in range(len(num))]


if __name__ == '__main__':
    num1, num2 = input('Число А: ').upper(), input('Число B: ').upper()
    print(f'{num_list(num1)} + {num_list(num2)} = {sum_hex(num1, num2)}')
    print(f'{num_list(num1)} * {num_list(num2)} = {multiply_hex(num1, num2)}')
