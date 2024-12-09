# методы строк
print('# методы строк')

## методы меняющие регистр
print('## методы меняющие регистр')
str1 = 'Python is Awesome'
print(str1.upper())  # PYTHON IS AWESOME
print(str1.lower())  # python is awesome
print(str1.capitalize())  # Python is awesome
print(str1.title())  # Python Is Awesome
print(str1.swapcase())  # pYTHON IS aWESOME

print()
## методы проверки (для условий if, циклов while и т.д.)
print('## методы проверки')
str2 = 'Python Is Awesome'
# .isupper() - проверяет, является ли вся строка в верхнем регистре
print(str2.isupper())  # False
# .islower() - проверяет, является ли вся строка в нижнем регистре
print(str2.islower())  # False
# .istitle() - проверяет, начинается ли каждое слово строки с заглавных букв
print(str2.istitle())  # True
# .isalpha() - проверяет, состоит ли строка только из букв, пробел не считается буквой
print(str2.isalpha())  # False
# .isalnum() - проверяет, состоит ли строка только из букв, цифр, пробел не считается буквой
print(str2.isalnum())  # False
# методы проверки числа
print(str2.isnumeric())  # False
print(str2.isdecimal())  # False
print(str2.isdigit())  # False
# .isascii() - проверяет, является ли строка ASCII
print(str2.isascii())  # False

print()
## методы замены
print('## методы замены')
str3 = 'Python is Awesome'
# .replace() - заменяет все вхождения подстроки в строке на другую подстроку
print(str3.replace('Python', 'Java'))  # Java is Awesome

# .strip() - удаляет пробелы в начале и в конце строки
# .lstrip() - удаляет пробелы в начале строки
# .rstrip() - удаляет пробелы в конце строки
str4 = '   Python is Awesome   '
print(str4.strip())  # 'Python is Awesome'
print(str4.lstrip())  # 'Python is Awesome   '
print(str4.rstrip())  # '   Python is Awesome'

print()
## методы разделения и слияния
print('## методы разделения и слияния')
str5 = 'Python is Awesome'
# .split() - разбивает строку на список по разделителю
# по умолчанию разбивает строку по пробелу
print(str5.split())  # ['Python', 'is', 'Awesome']
print(str5.split(' '))  # ['Python', 'is', 'Awesome']
print(str5.split('o'))  # ['Pyth', 'n is Awes', 'me']
# .join() - объединяет список в строку
# по умолчанию объединяет список по пробелу
print(' '.join(['Python', 'is', 'Awesome']))  # Python is Awesome
print('-'.join(['Python', 'is', 'Awesome']))  # Python-is-Awesome
print('*'.join(['Python', 'is', 'Awesome']))  # Python*is*Awesome
list_to_join = ['JS', 'PHP', 'Python']
str_for_join = '/'
print(str_for_join.join(list_to_join))  # JS/PHP/Python

print()
## методы поиска и подсчёта
print('## методы поиска и подсчёта')
str6 = 'Python is Awesome and so is Java'
# .find() - возвращает индекс первого вхождения подстроки в строку
print(str6.find('is'))  # 7
# .count() - возвращает количество вхождений подстроки в строку
print(str6.count('is'))  # 2
# .index() - возвращает индекс первого вхождения подстроки в строку
print(str6.index('is'))  # 7
# можно задавать начальную позицию для поиска
print(str6.index('is', 10))  # 25
# .rindex() - возвращает индекс последнего вхождения подстроки в строку
print(str6.rindex('is'))  # 25

# .find() возвращает -1, если подстрока не найдена
# .index() возвращает ValueError, если подстрока не найдена
print(str6.find('JS'))  # -1
# print(str6.index('JS'))  # ValueError: substring not found

print()
## len() - возвращает длину строки
print('## len() - возвращает длину строки')
str7 = 'Python is Awesome and so is Java'
print(len(str7))  # 31
