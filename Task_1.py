data = {}
amount = int(input('Количество предприятий: '))
for num in range(amount):
    name = input(f'Название {num + 1}-го предприятия: ')
    profit_year = []
    for i in range(4):
        profit = int(input(f'Прибыль предприятия {name} за {i + 1}-й квартал: '))
        profit_year.append(profit)
    data[name] = profit_year
# значения ключей словаря сделал списком, чтобы при необходимости иметь доступ в квартальным значениям прибыли.
sum_profit = 0
for key in data:
    sum_profit += sum(data.get(key))

avg_profit = sum_profit / amount

print(f'Средняя прибыль (за год для {amount}-х предприятий): {avg_profit:.2f}')

for key in data:
    profit_year = sum(data.get(key))
    if profit_year > avg_profit:
        print(f'Прибыль предприятия {key}: {profit_year}, что больше средней на {profit_year - avg_profit:.2f}')
    elif profit_year < avg_profit:
        print(f'Прибыль предприятия {key}: {profit_year}, что меньше средней на {avg_profit - profit_year:.2f}')
    else:
        print(f'Прибыль предприятия {key}: {profit_year} равна среднему значению')
