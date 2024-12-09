# Задача 1: Анализ данных о сотрудниках
# У вас есть словарь, содержащий информацию о сотрудниках компании.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите имена всех сотрудников.
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
# 4. Обновите зарплату "Alice" до 5500.
# 5. Удалите сотрудника "Charlie".
# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
#
employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
}

# 1.
print('# 1')
for name in employees:
    print(name)

# 2.
print('\n# 2')
total_salary = 0
for employee in employees.values():
    total_salary += employee['salary']
print(f'Общая зарплата всех сотрудников: {total_salary}')

# 3.
print('\n# 3')
employees['David'] = {"age": 28, "department": "IT", "salary": 6500}
print(employees)

# 4.
print('\n# 4')
employees['Alice']['salary'] = 5500
print(employees)

# 5.
print('\n# 5')
del employees['Charlie']
print(employees)

# 6.
print('\n# 6')
for name, info in employees.items():
    # age, department, salary = info.values()
    # print(f"Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}")
    print(f"Имя: {name}, Возраст: {info['age']}, Отдел: {info['department']}, Зарплата: {info['salary']}")



# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите названия всех товаров.
# 2. Увеличьте количество "Apples" на 10.
# 3. Измените цену "Bananas" на 1.5.
# 4. Удалите товар "Cherries".
# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
#
inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}

print('#1')
for good in inventory:
    print(good)

print('#2')
inventory['Apples']['quantity'] = 50 + 10
print(inventory)

print('#3')
inventory['Bananas']['price'] = 1.5
print(inventory)

print('#4')
del inventory['Cherries']
print(inventory)

print('#5')
inventory['Dates']= {"quantity": 15, "price": 4}
print(inventory)

print('#6')
print(int(inventory['Apples']['quantity']) * int(inventory['Apples']["price"]) + int(inventory['Bananas']['quantity']) * int(inventory['Dates']["price"]) + int(inventory['Dates']['quantity']) * int(inventory['Bananas']["price"]))
