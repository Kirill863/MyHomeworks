# Задача 1: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}
def create_dict(k, v):
    result_dict = {}
    for i in range(len(k)):
        result_dict[k[i]] = v[i]

    return result_dict


keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
print(create_dict(k=keys, v=values))


# Задача 2: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

print(count_characters("hello world"))


# Задача 3: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)

def sum_positive_negative(*args):
    positive_sum = 0
    negative_sum = 0

    for number in args:
        if number > 0:
            positive_sum += number
        elif number < 0:
            negative_sum += number

    return positive_sum, negative_sum


result = sum_positive_negative(1, -2, 3, -4, 5)
print(result)  

sum_positive_negative(1, -2, 3, -4, 5)

# Задача 4: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York

def generate_string(**kwargs):
    # Используем генератор списка для создания пар "ключ=значение"
    pairs = [f"{key}={value}" for key, value in kwargs.items()]

    # Объединяем пары в одну строку через запятую
    result = ', '.join(pairs)

    return result

formatted_string = generate_string(name="Alice", age=30, city="New York")
print(formatted_string)
