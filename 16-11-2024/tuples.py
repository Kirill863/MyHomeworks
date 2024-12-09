# кортежи — неизменяемая коллекция
print()
print('# создание кортежей')

my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))

my_tuple = 1, 2, 3
print(my_tuple)
print(type(my_tuple))

my_tuple = (1,)
print(my_tuple)
print(type(my_tuple))

my_tuple = 1,
print(my_tuple)
print(type(my_tuple))


names = ('Bob', 'Alice', 'Charlie')
print(names[0])
# names[0] = 'David'  # TypeError: 'tuple' object does not support item assignment

print()
# Методы кортежа
print('# Методы кортежа')
person = ("Alice", [30, "New York"], 35000, "Alice", "Alice")
print(person.count("Alice"))  # Вывод: 3
print(person.index(35000))  # Вывод: 2
print(person.index('Alice'))  # Вывод: 0
print(person.index('Alice', 1))  # Вывод: 3

print()
print(person)
person[1][1] = 'San Francisco'
print(person)

# names = ['Bob', 'Alice', 'Charlie']
# cities = ['New York', 'San Francisco', 'London']
# emails = ['9V8j0@example.com', '2G4mM@example.com', 'B2b9A@example.com']
