# цикл for
# for переменная in последовательность:
#     тело цикла

# cities = ['Amsterdam', 'Berlin', 'Capetown', 'Dublin', 'Ekaterinburg']

# print()
# i = 0
# while i < len(cities):
#     print(cities[i])
#     i += 1
# print()

# print()
# for city in cities:
# # на каждой итерации city принимает значения: Amsterdam, Berlin, ...
#     print(city)
# print()

# range(start, stop, step)

# если мы задаём только один параметр, то это будет stop
# то есть range примет значения от 0 до stop (не включительно) с шагом 1

# print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(6)))  # [0, 1, 2, 3, 4, 5]

# если мы задаём два параметра, то это будет start и stop
# то есть range примет значения от start до stop (не включительно) с шагом 1

# print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(90, 100)))  # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# если мы задаём три параметра, то это будет start, stop и step
# то есть range примет значения от start до stop (не включительно) с шагом step

# print(list(range(1, 11, 2)))  # [1, 3, 5, 7, 9]
# print(list(range(10, 100, 10)))  # [10, 20, 30, 40, 50, 60, 70, 80, 90]

# range() так же может иметь отрицательный шаг
# print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(list(range(-10, -60, -10)))  # [-10, -20, -30, -40, -50]

# range() не проверяет ошибочность прогрессии,
# то есть для list(range(1, 10, -1)) он вернёт [] — пустой список

# for и range
# range в цикле не обязательно преобразовывать в список
# for i in range(10, 100, 10):
#     print(i)
# >>> 10
# >>> 20
# >>> 30
# >>> 40
# >>> 50
# >>> 60
# >>> 70
# >>> 80
# >>> 90

# _ переменную можно использовать в цикле, если нам ничего не 
# нужно с нею работать
# for _ in range(10):
#     print('Hello')

# enumerate(коллекция, начальное значение)
# позволяет получить индекс элемента в цикле
# возвращает два значения: индекс и элемент

countries = ['Austria', 'Belgium', 'Croatia', 'Denmark', 'Estonia']
# for country in countries:
#     print(country)
# >>> Austria
# >>> Belgium
# >>> Croatia
# >>> Denmark
# >>> Estonia

# i = 1
# for country in countries:
#     print(i, country)
#     i += 1
# >>> 1 Austria
# >>> 2 Belgium
# >>> 3 Croatia
# >>> 4 Denmark
# >>> 5 Estonia

# for i, country in enumerate(countries):
#     print(i, country)
# >>> 0 Austria
# >>> 1 Belgium
# >>> 2 Croatia
# >>> 3 Denmark
# >>> 4 Estonia


# for i, country in enumerate(countries, 1):
#     print(i, country)
# >>> 1 Austria
# >>> 2 Belgium
# >>> 3 Croatia
# >>> 4 Denmark
# >>> 5 Estonia

# строка это тоже коллекция
# for letter in 'Hello':
#     print(letter)
# >>> H
# >>> e
# >>> l
# >>> l
# >>> o

# число не является коллекцией
# for digit in 12345:
#     print(digit)
# >>> TypeError: 'int' object is not iterable  