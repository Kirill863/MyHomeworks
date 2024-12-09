# Списки
# списки в Python и массивы в JS — примерно одно и то же.
print('Списки')

rand_list = [1, 'two', 3.0, True, False, None]
print(rand_list)
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
print(fruits)

print('Доступ к элементам списка')
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])
print(fruits[:])

fruits[1] = 'kiwi'
print(fruits)

print()
print('Индексация и срезы')
print(fruits[0])  # [-6]
print(fruits[1])  # [-5]
print(fruits[2])  # [-4]
print(fruits[3])  # [-3]
print(fruits[4])  # [-2]
print(fruits[5])  # [-1]

print()
users = ['John', 'Jane', 'Bob', 'Alice']
print(users[2])
orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
messages = ['Hello', 'Hi', 'How are you?', 'Goodbye', 'See you later']

print()
# пустой список
empty_list = []
print(empty_list)
empty_list = list()
print(empty_list)

list_with_space = ['']
print(list_with_space)


# при попытке записать значения одного списка в другой
# мы просто получаем ссылку на один и тот же список
a = [1, 2, 3]
b = a
print(a)
# >>> [1, 2, 3]
print(b)
# >>> [1, 2, 3]
b[0] = -5
print(b)
# >>> [-5, 2, 3]
print(a)
# >>> [-5, 2, 3]
print(id(a))
# >>> 2788661012864
print(id(b))
# >>> 2788661012864
a[1] = 9
print(a)
# >>> [-5, 9, 3]
print(b)
# >>> [-5, 9, 3]

# чтобы скопировать значения одного списка в другой
# можно использовать срез по всему списку
x = [10, 20, 30]
y = x[:]
id(x)
# >>> 2788661010688
id(y)
# >>> 2788661011968
y[0] = 5
print(y)
# >>> [5, 20, 30]
print(x)
# >>> [10, 20, 30]
# можно использовать метод copy()
y = x.copy()
print(y)
# можно использовать распаковку
y = [*x]
print(y)
# можно использовать функцию list()
y = list(x)
print(y)

print()
# вложенные списки
print('# вложенные списки')
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0])
print(matrix[1][1])

# пример приближенный к реальности
users = [
    ['John', 'Smith', 25, True],
    ['Jane', 'Doe', 30, False],
    ['Bob', 'Johnson', 35, True]
]

employees = [
    ['John', 'Smith', 25, ['Java', 'Python']],
    ['Jane', 'Doe', 30, ['JavaScript', 'TypeScript']],
    ['Bob', 'Johnson', 35, ['C++', 'C#']]
]

print(employees[1][3][1])  # TypeScript
