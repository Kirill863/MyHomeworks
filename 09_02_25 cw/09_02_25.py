"""
Аннотации типов данных
"""

# from typing import List, Tuple, Set, Dict, Callable, Iterable, Iterator, Any, Union, Optional

# list_num = ["1", 2, 3, 4, 5]

# def func(num: List[Union[int, str]]) -> None:
#     print(list_num)

# func(list_num)

# class MyClass:
#     pass

# cl: MyClass = MyClass()

# def alphd_func(func: Callable[[List[int]], None]):
#     pass

'''
"""
Тема: Функции. Области видимости. Замыкания. Декоратор. Урок: 25
- Области видимости
Buit-in - встроенная
Global - глобальная
Local - локальная
Nonlocal - нелокальная
"""

# Buit-in - встроенная
# print()
# len()
# sum()
# bool()

# Global - глобальная - область видимости файла
a = 5


# Local - область видимости внутри функций \ методов
def func():
    a = 10
    print(a)

def func2():
    a = 15
    print(a)

def func3():
    print(a)

def func4(a: int) -> None:
    """
    Печатает число
    :param a: число для печати
    """
    print(a)

def func6():
    global a, b
    a = 20
    b = 22
    print(f'{a=} внутри ')

# print = "печенька"
# print("!") # 'str' object is not callable

# Проверим a
print(f'{a=}')

# Вызов 2 функций
func()
func2()

# Проверим a
print(f'{a=}')

# Вызов функции 6
func6()

# Проверим a
print(f'{a=}')

# Проверим b
print(f'{b=}')

def func7():
    a = 7
    print(f'Функция 7 {a=}')

    def built7():
        # В зависимости от наличия строки, а в func7 будет / не будет перписываться
        nonlocal a 
        a = 77
        print(f'Встроенная функция 7 {a=}')

    built7()
    print(f'Функция 7 после вызова built7 {a=}')

# Вызов функции 7
func7()
# Функция 7 a=7
# Встроенная функция 7 a=77
# Функция 7 после вызова built7 a=77

'''
"""
def fucn(a):
    # a - хранится тут
    def inner():
        # a - используется тут
        print(a)
    return inner

banan = print
banan("Привет!")

# Вызов функции 8
foo = fucn8("пирожок")
foo()
"""
# функция - счетчик работабщая на замыканиях

"""
def counter(start_value: int)-> Callable[[], int]:
    def step():
        nonlocal start_value
        start_value += 1
        return start_value
    return step

# Создаем счетчики

counter1 = counter(10)
counter2 = counter(20)

print(counter1())
print(counter2())
print(counter1())
print(counter2())
print(counter1())
print(counter2())
"""

# функция с кещированием

# shop_list = ['Айфон' , 'Айпад' , 'MacBook']

"""
Тема: Функции. Аннотации типов. Typing. Декораторы. Урок: 26
"""

from typing import Callable


# Функция с кешированием

# def cach_sorter() -> Callable[[list[str]], list[str]]:
#     cach = []
#     last_input = []
    
#     def sorter(data: list[str]) -> list[str]:
#         nonlocal cach, last_input
#         if data != last_input:
#             print('Делаем сортировку')
#             cach = sorted(data)
#             last_input = data.copy()
#             return cach
#         print("Возвращаем кеш!")
#         return cach
    
#     return sorter


# sorter_ = cach_sorter()
# shop_list = ["Iphone", "Ipad", "MacBook", "Пирожок"]

# # Тестируем
# print(sorter_(shop_list))
# print(sorter_(shop_list))
# shop_list.append("RTX5090")
# print(sorter_(shop_list))
# print(sorter_(shop_list))

# Декоратор

def decorator_1(func:Callable):
    def wrapper():
        print("До вызова функции")
        func()
        print("после вызова функции")
    return wrapper

def print_hello():
    print("Hello!")

def print_goodbay():
    print("Goodbay!")

print_hello_decarated = decorator_1(print_hello)
print_goodbay_decarated = decorator_1(print_goodbay)

print_hello_decarated()
print_goodbay_decarated()

def decorator_2(func: Callable[[str], [str]]):
    def wrapper(s: str) -> str:
        print("До вызова функции")
        result = func(s)
        print('После вызова функции')
        return result
    
    return wrapper

def print_hello_2 (s: str) -> str:
    return f"Hello 2, {s}"

print_hello_2_decarated = decorator_2(print_hello_2)
print(print_hello_2_decarated("Анатолий"))

@decorator_2
def print_goodbay_2(s: str) -> str:
    return f"Goodbay 2, {s}"

print(print_goodbay_2("Анатолий"))

def check_lenth_string_decorator(lenght: int = 10) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(name: str):
            if len(name) > lenght:
                raise ValueError(f"Длина строки {name} ,больше {lenght}") 
            else:
                return func(name)
        
        return wrapper
    return decorator

@check_lenth_string_decorator()
def say_my_name(name: str) -> str:
    return(f"Привет, {name}!")

print(say_my_name("Анатолий"))
print(say_my_name("Анатолий Степанович"))