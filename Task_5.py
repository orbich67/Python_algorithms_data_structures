a = ord(input('1-я буква: ').lower())
b = ord(input('2-я буква: ').lower())
value_a = a - ord('a') + 1
value_b = b - ord('a') + 1
print(f'Места букв в алфавите {chr(a)} - {value_a} и {chr(b)} - {value_b}')
print(f'Между буквами {chr(a)} и {chr(b)} {abs(value_a - value_b) - 1} букв')
