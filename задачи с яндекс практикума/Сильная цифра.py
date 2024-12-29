# Ввод числа
number = input()

# Преобразование введенной строки в список цифр
digits = list(str(number))

# Инициализация максимальной цифры первым элементом списка
max_digit = digits[0]

# Цикл для нахождения максимальной цифры
for digit in digits:
    if digit > max_digit:
        max_digit = digit

# Вывод максимальной цифры
print(max_digit)
