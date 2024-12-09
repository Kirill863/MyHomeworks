print()


def add2(a, b):
    return a + b


print(add2(10, 15))

# print(add2(10, 15, 20))  # TypeError: add() takes 2 positional arguments but 3 were given


def add3(a, b, c):
    return a + b + c


print(add3(10, 15, 20))
# print(print(add3(10, 15, 20, 25)))  # TypeError: add3() takes 3 positional arguments but 4 were given
print()


# *args — произвольное количество позиционных (не именованных) аргументов
# args — просто название, оно может быть любым
# *args — это кортеж значений
def add(*args):
    # print(args)
    accumulator = 0
    for i in args:
        accumulator += i
    return accumulator


print(add(1, 2, 3, 4, 5, 6, 7))
print(add(6, 7))
print(add(4, 5, 6, 7, 3, 2, 1, 11, 12, 13, 9, 8))

print()
def get_sum_odds_evens(*args):

    odd_sum = 0
    even_sum = 0

    for i in args:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    return odd_sum, even_sum

x, y = get_sum_odds_evens(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(x, y)

print()
# **kwargs — произвольное количество именованных (не позиционных) аргументов
# kwargs — просто название, оно может быть любым
# kwargs — это словарь значений

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("-" * 20)


describe_person(name="Alice", age=30, city="New York")
describe_person(name="Bob", age=25, country="USA")
describe_person(name="Charlie", age=35, city="London", country="UK")

print()