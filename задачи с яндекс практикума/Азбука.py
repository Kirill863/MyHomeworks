"""Знакомые нам воспитанники детского сада наконец-то начали учить буквы.
Воспитатель предложил ребятам назвать слова, которые начинаются с А, Б или В. Напишите программу, которая проверяет, что первая буква во всех словах — А, Б или В.

Формат ввода
Вводится натуральное число 
N
N — количество слов, названных детьми.
В каждой из последующих 
N
N строк записано по одному слову строчными буквам.

Формат вывода
YES — если все слова начинаются с нужной буквы.
NO — если хотя бы одно слово начинается не с нужной буквы."""

N = int(input())

slova = []
for _ in range(N):
    slovo = input()
    slova.append(slovo)

all_correct = True
for slovo in slova:
    if slovo[0] not in ["а", "б", "в"]:
        all_correct = False
        break

if all_correct:
    print("YES")
else:
    print("NO")


