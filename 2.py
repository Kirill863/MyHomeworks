num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

max_num = num1

if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3

print(f"Наибольшее число: {max_num}")
