import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Проверка на тривиальный случай
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
else:
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        print("No solution")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("{:.2f}".format(x))
    else:
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        # Сортировка корней в порядке возрастания
        if x_1 < x_2:
            print("{:.2f} {:.2f}".format(x_1, x_2))
        else:
            print("{:.2f} {:.2f}".format(x_2, x_1))
