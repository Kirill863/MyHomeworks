print()
print('# Создание словарей')

print('# Способ 1: фигурные скобки')
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print(person['age'])
print(person['name'])
print(person['city'])
print(person)
# индексации в словарях нет, вместо этого используются ключи
# print(person[1])  # KeyError: 1

print()
print('# Способ 2: функция dict')
person = dict(name='John', age=30, city='New York')
print(person['age'])
print(person['name'])
print(person['city'])
# person['country']  # KeyError: 'country'
print(person)

print()
print('# Изменение словаря и добавление данных')
person['age'] = 31
person['city'] = 'San Francisco'
print(person)

person['country'] = 'USA'
print(person)

print()
print('## Методы словарей')

print('.get() — # Проверка наличия ключа')
# .get() — первое значение - ключ, второе значение - значение по умолчанию
# словарь при этом не меняется
print(person.get('age'))
print(person.get('age', 18))
print(person.get('salary'))  # None
print(person.get('salary', 0))  # 0
print(person)

print()
print('.setdefault() — # Проверка наличия ключа')
# .setdefault() — первое значение - ключ, второе значение - значение по умолчанию
# если в словаре не было такого ключа, то он добавляется
person.setdefault('age')
person.setdefault('age', 18)
print(person)
person.setdefault('salary', 0)
print(person)

print()
print('.fromkeys() — # Создание словаря из списка ключей')
# .fromkeys() — первое значение - список ключей, второе значение - значение по умолчанию
countries = ['Argentina', 'Brasil', 'Chile', 'Colombia']
countries_dict = dict.fromkeys(countries)
print(countries_dict)
countries_dict = dict.fromkeys(countries, 'South America')
print(countries_dict)

print()
print('.clear() — # Очистка словаря')
print(person)
person.clear()
print(person)

print()
print('.pop() — # Удаление элемента из словаря по ключу и возврат его значение')
# '.pop() — первое значение - ключ, по которому удаляется элемент
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
person_age = person.pop('age')
print(person_age)
print(person)

print()
print('.popitem() — # Удаление последнего добавленного элемента в словарь')
# '.popitem() — удаляет последний элемент в словаре и возвращает ПАРУ ключ-значение
person['salary'] = 5000
print(person)
person_salary = person.popitem()
print(person_salary)
print(person)

print()
print('.copy() — # Копирование словаря')
# '.copy() — возвращает копию словаря
person_wrong_copy = person
print(id(person), id(person_wrong_copy))
person_copy = person.copy()
print(id(person), id(person_copy))

print()
print('len() — # Подсчет количества ключей в словаре')
print(len(person))  # 2

print()
print('in, not in — # Проверка наличия ключа в словаре')
print('name' in person)  # True
print('name' not in person)  # False
print('country' in person)  # False
print('country' not in person)  # True