"""
Функции. Области видимости. Замыкания. Декоратор
Buit-in - встроенная
Global - глобальная
Local - локальная
Nonlocal - нелокальная

Buit-in - встроенная
print(), len(), 

Global - глобальная
a = 5

Local - локальная внутрь функции или метода

def func():
    a = 10
    print(a)

def func2():
    a = 15
    print(a)


"""
print(f'{a=}')

def func7():
    a = 7
    print(f"Функция 7 {a=}")

    def built7():
        nonlocal a
        a = 77
        print(f'Всьроенная функция 7 {a=}')
    
    built7()
    print(f'Функция 7 после вызова built7 {a=}')

func7()

def func8(a):
    def inner8():
        print(a)
    return inner8

foo = func8(10)
foo()
