row = 0
for num in range(32, 127 + 1):
    print(f'{num} - "{chr(num)}"', end=', ')
    row += 1
    if row % 10 == 0:
        print('\n')
