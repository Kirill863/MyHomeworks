# Тема: Цикл for
#
# Упражнение 1: Подсчет гласных в строке
#
# Напишите программу, которая принимает строку от пользователя и подсчитывать количество гласных букв (a, e, i, o, u)
# в этой строке.
# Используйте цикл for и условие if.


vowels = 'aeiou'
count = 0
user_input = input("Введите строку: ")

for char in user_input:
    if char in vowels:
        count += 1
print(f'Количество гласных: {count}')


# Упражнение 2: Генерация и вывод последовательности чисел
#
# Напишите программу, которая генерит и выводит последовательность чисел от 1 до 20,
# но выводит "Fizz" вместо чисел, кратных 3, "Buzz" вместо чисел, кратных 5, и "FizzBuzz"
# вместо чисел, кратных как 3, так и 5.
# Используйте цикл for и функцию range.

import random

numbers = [random.randint(1, 20) for _ in range(10)]
print("Случайные числа:", numbers)

for index in range(len(numbers)):
    number = numbers[index]
    if number % 3 == 0 and number % 5 == 0:
        numbers[index] = "FizzBuzz"
    elif number % 3 == 0:
        numbers[index] = "Fizz"
    elif number % 5 == 0:
        numbers[index] = "Buzz"

print("Список с заменами:", numbers)


