def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Ввод числа
number = int(input("Введите неотрицательное число: "))
# Проверка на неотрицательность
if number < 0:
    print("Введите неотрицательное число.")
else:
    # Вывод факториала
    print(f"Факториал {number} равен {factorial(number)}")
