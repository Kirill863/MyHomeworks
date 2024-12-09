import math

a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))

d = b * 2 - 4 * a * c
if d < 0:
    print('No solution')
elif d == 0:
    x = -b / 2 * a
    print(x)
elif d > 0:
    x_1 = (-b + math.sqrt(d)) / 2 * a
    x_2 = (-b - math.sqrt(d)) / 2 * a
    if x_1 > x_2:
        print(x_2, x_1)
    elif x_1 < x_2:
        print(x_1, x_2)