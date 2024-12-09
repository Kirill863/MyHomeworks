print()


def greet(name):
    print(f"Hello, {name}!")

# именование функций
# snake_case
# всё в нижнем регистре
# имена переменных — существительные
# имена функций — глаголы


greet("John")
greet('Alice')

print()
x = len([1, 2, 3])
print(x)

print()
y = greet('Bob')
print(y)

print()
print(print('Hello world!'))


# оператор return
print()
# функция для сложения двух чисел
def add(a, b):
    return a + b


# параметры
sum_1_2 = add(1, 2)
print(sum_1_2)

sum_3_4 = add(3, 4)
print(sum_3_4)

sum_5_6 = add(a=5, b=6)
print(sum_5_6)

print()
# параметры по умолчанию
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")
greet("Bob", "Hi")


# def print(*args, sep=' ', end='\n'):
#     print(*args, sep=sep, end=end)

print()
# возврат нескольких значений
def get_square_cube(x):
    square = x ** 2
    cube = x ** 3
    return square, cube


square_of_7, cube_of_7 = get_square_cube(7)
print(square_of_7, cube_of_7)

tuple_result = get_square_cube(7)
print(tuple_result)


print()