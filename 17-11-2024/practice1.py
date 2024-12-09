# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)

def analyze_numbers(numbers):
    sum = numbers[0] + numbers[1] + numbers[2]+ numbers[3] + numbers[4] + numbers[5]
    sred = sum / 6
    chet = 0
    for i in numbers:
        if i % 2 == 0:
            chet = chet + 1
    print(sum, sred, chet)
analyze_numbers(numbers)





# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
strings = ["apple", "banana", "cherry", "date"]
# Вывод функции: ('banana', 'date', 3)

def analyze_strings(strings):
    max_str = max(strings, key=len)
    min_str = min(strings, key=len)
    a = 0
    for string in strings:
        if 'a' in string:
            a += 1
    print(max_str, min_str, a)
analyze_strings(strings)

# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')

# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')

def analyze_salaries(employees):
    salaries = list(employees.values())
    avg_salary = sum(salaries) / len(salaries)
    max_salary = max(salaries)

    for name in employees:
        if employees[name] == max_salary:
            max_salary_employee = name

    # max_salary_employee = max(employees, key=employees.get)

    return avg_salary, max_salary, max_salary_employee


print(analyze_salaries({"Alice": 5000, "Bob": 7000, "Charlie": 6000}))

# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]).
#
def filter_numbers(numbers):

    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    return (even_numbers, odd_numbers)

result = filter_numbers(numbers)
print(result)
