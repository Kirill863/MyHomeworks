"""Сложение чисел весьма простая задача.
К сожалению, пользователи не всегда вводят данные так, как нам удобно.

Формат ввода
Два целых числа, разделённые пробелом.

Формат вывода
Одно целое число — сумма переданных чисел."""

# получаем данные от пользователя
vvod = input()

# разделяем строку на два числа
new_vvod = vvod.split()

# преобразуем строки в целые числа
num1 = int(new_vvod[0])
num2 = int(new_vvod[1])

# вычисляем сумму
sum_vvod = num1 + num2

# выводим результат
print(sum_vvod)
