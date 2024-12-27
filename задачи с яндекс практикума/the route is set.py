"""Навигация была важна во все времена.
Нам достался архив маршрутов движения, но их оказалось так много, что без автоматизации мы с ними не справимся вовек. Каждый маршрут представляет собой последовательность шагов в одном из четырех направлений:

СЕВЕР;
ВОСТОК;
ЮГ;
ЗАПАД.
Напишите программу, чтобы по заданному маршруту она определяла, в какой именно точке мы окажемся.
Для простоты будем считать, что в начале маршрута мы находимся в точке (0; 0).

Формат ввода
Вводятся инструкции маршрута в виде:
<направление>
<количество шагов>
Ввод завершается строкой СТОП.

Формат вывода
Два целых числа — координаты конечной точки маршрута."""

x = 0
y = 0

direction = input()
number_of_steps = int(input())

while direction != "СТОП":
    if direction == "СЕВЕР":
        y += number_of_steps
    elif direction == "ЮГ":
        y -= number_of_steps
    elif direction == "ВОСТОК":
        x += number_of_steps
    elif direction == "ЗАПАД":
        x -= number_of_steps

    # Обновляем значение direction и number_of_steps внутри цикла
    direction = input()
    if direction != "СТОП":
        number_of_steps = int(input())

print(y)
print(x)

