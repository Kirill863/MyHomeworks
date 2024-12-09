# функция len()
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
print(len(fruits))

numbers = [1, 2, 3, 4, 5]
# функция min()
print(min(fruits))
# >>> 'apple'
print(min(numbers))
# >>> 1
# функция max()
print(max(fruits))
# >>> 'fig'
print(max(numbers))
# >>> 5

print()
# метод .append() добавляет элемент в конец списка
# используется когда мы хотим добавить один элемент
fruits.append('grape')
print(fruits)
# >>> ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

print()
# метод .extend() добавляет элементы в конец списка
# используется когда мы хотим добавить несколько элементов
# они обязательно должны быть заключены в список (в квадратных скобках)
fruits.extend(['kiwi', 'lemon'])
print(fruits)
# >>> ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'kiwi', 'lemon']

# fruits.extend('mango')
# print(fruits)
# >>> ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'kiwi', 'lemon', 'm', 'a', 'n', 'g', 'o']

print()
numbers = [1, 2, 3, 4, 5, 6]
# метод .insert() добавляет элемент в список по указанному индексу
numbers.insert(2, 2.5)
print(numbers)
# >>> [1, 2, 2.5, 3, 4, 5, 6]

print()
# метод .remove() удаляет элемент из списка
numbers.remove(2.5)
print(numbers)
# >>> [1, 2, 3, 4, 5, 6]
numbers.append(6)
print(numbers)
# >>> [1, 2, 3, 4, 5, 6, 6]
numbers.remove(6)
print(numbers)
# >>> [1, 2, 3, 4, 5, 6]

print()
# метод .pop() удаляет последний элемент списка и возвращает его
last_number = numbers.pop()
print(last_number)
# >>> 6
print(numbers)
# >>> [1, 2, 3, 4, 5]

# можно указать индекс
first_number = numbers.pop(0)
print(first_number)
# >>> 1
print(numbers)
# >>> [2, 3, 4, 5]

print()
# метод .clear() очищает список
numbers.clear()
print(numbers)
# >>> []

print()
# метод .index() возвращает индекс первого вхождения элемента
numbers = [1, 2, 3, 2, 2]
index_of_2 = numbers.index(2)
print(index_of_2)
# >>> 1

# можно указать начало поиска
index_of_second_2 = numbers.index(2, 2)
print(index_of_second_2)
# >>> 3

print()
# метод .count() возвращает количество вхождений элемента в списке
numbers = [1, 2, 3, 2, 2]
count_of_2 = numbers.count(2)
print(count_of_2)
# >>> 3

print()
# метод .reverse() переворачивает список
# меняет сам список
fruits = ['date', 'banana', 'apple', 'fig', 'cherry', 'elderberry']
fruits.reverse()
print(fruits)
# >>> ['fig', 'elderberry', 'date', 'cherry', 'banana', 'apple']

# функция reversed() возвращает итератор, который переворачивает список
# не меняет сам список
# нужно сохранять результат выполнения
fruits = ['date', 'banana', 'apple', 'fig', 'cherry', 'elderberry']
reversed_fruits = list(reversed(fruits))
print(reversed_fruits)
# >>> ['elderberry', 'cherry', 'fig', 'apple', 'banana', 'date']

print()
# метод .sort() сортирует список
# меняет сам список
fruits = ['date', 'banana', 'apple', 'fig', 'cherry', 'elderberry']
fruits.sort()
print(fruits)
# >>> ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# функция sorted() возвращает отсортированный список
# не меняет сам список
# нужно сохранять результат выполнения
fruits = ['date', 'banana', 'apple', 'fig', 'cherry', 'elderberry']
sorted_fruits = sorted(fruits)
print(sorted_fruits)
# >>> ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

print()
# метод .copy() создает копию списка
fruits = ['date', 'banana', 'apple', 'fig', 'cherry', 'elderberry']
copied_fruits = fruits.copy()
print(copied_fruits)
# >>> ['date', 'banana', 'apple', 'fig', 'cherry', 'elderberry']
print(id(fruits))
# >>> 2788661010688
print(id(copied_fruits))
# >>> 2788661011968


print()
# изменяемость списков и неизменяемость строк
s = 'Hello'
print(id(s))
# >>> 2154065903152
s += 'World'
print(id(s))
# >>> 2154065396208

l = [1, 2, 3]
print(id(l))
# >>> 2154068918848
l += [4, 5]
print(l)
[1, 2, 3, 4, 5]
print(id(l))
# >>> 2154068918848

x = 10
print(id(x))
# >>> 140722918618184
print(x)
# >>> 10
x += 1
print(id(x))
# >>> 140722918618216
print(x)
# >>> 11


# изменяемые типы данных: списки (list), словари (dict), множества (set)
# неизменяемые типы данных: строки (str), числа (int, float), кортежи (tuple), замороженные множества (frozenset)