"""Во многих играх порядок ходов определяется броском кубика или монетки, а в нашей первым ходит тот, чье имя лексикографически меньше. Определите, кто из игроков будет ходить первым.

Формат ввода
В первой строке записано одно натуральное число N N — количество игроков. В каждой из последующих N N строк указано одно имя игрока.

Формат вывода
Имя игрока, который будет ходить первым."""

# Чтение количества игроков
N = int(input())

# Инициализация списка для хранения имен игроков
имена_игроков = []

# Чтение имен игроков
for _ in range(N):
    имя = input()
    имена_игроков.append(имя)

# Определение лексикографически наименьшего имени
наименьшее_имя = min(имена_игроков)

# Вывод лексикографически наименьшего имени
print(наименьшее_имя)
