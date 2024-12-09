print()
print('# множества')

my_set = {2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 6, 7, 1, 2, 1, 2}
print(my_set)

# вывод количества элементов
print(len(my_set))

# добавление элемента
my_set.add(8)
print(my_set)

# удаление элемента, если такого элемента нет, то вернётся ошибка
my_set.remove(1)
print(my_set)

# удаление элемента, если такого элемента нет, то ошибка не вернётся
my_set.discard(3)
print(my_set)

# удаление всех элементов
my_set.clear()
print(my_set)