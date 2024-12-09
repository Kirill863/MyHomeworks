countries = {
    'Argentina': 'Buenos Aires',
    'Belgium': 'Brussels',
    'Chile': 'Santiago',
    'Denmark': 'Copenhagen',
    'Ecuador': 'Quito',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome'
}

print()
print('# перебор элементов словаря')
for i in countries:
    print(i)

print()
print('# перебор элементов словаря')
for key in countries:
    print(f'{key} — {countries[key]}')

print()
print('.keys() — возвращает список ключей словаря')
print(countries.keys())  # ['Argentina', 'Belgium', 'Chile', 'Denmark', 'Ecuador', 'France', 'Germany', 'Italy']

print()
print('.values() — возвращает список значений словаря')
print(countries.values())  # ['Buenos Aires', 'Brussels', 'Santiago', 'Copenhagen', 'Quito', 'Paris', 'Berlin', 'Rome']

print()
print('.items() — возвращает список пар ключ-значение')
print(countries.items())  # [('Argentina', 'Buenos Aires'), ('Belgium', 'Brussels'), ('Chile', 'Santiago'), ('Denmark', 'Copenhagen'), ('Ecuador', 'Quito'), ('France', 'Paris'), ('Germany', 'Berlin'), ('Italy', 'Rome')]

print()
print('# перебор значений словаря')
for value in countries.values():
    print(value)

print()
print('# перебор пар ключ-значение')
# for item in countries.items():
#     print(f'{item[0]} — {item[1]}')

# for item in countries.items():
#     country = item[0]
#     capital = item[1]
#     print(f'{country} — {capital}')

for country, capital in countries.items():
    print(f'{country} — {capital}')
