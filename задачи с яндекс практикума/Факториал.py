# Ввод числа от пользователя
number = int(input())

# Проверка, что введенное число является неотрицательным
if number < 0:
    print("Пожалуйста, введите неотрицательное число (0 или больше).")
else:
    result = 1
    for i in range(2, number + 1):
        result *= i
    print(result)
