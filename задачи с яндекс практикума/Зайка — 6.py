"""Очередное путешествие родителей с детьми, очередная игра с поиском зверушек за окном.
Давайте поиграем и найдём заек.

Формат ввода
В первой строке записано натуральное число 
N
N — количество выделенных придорожных местностей.
В каждой из 
N
N последующих строк записано описание придорожной местности.

Формат вывода
Количество заек."""

N = int(input())
zayka_count = 0

for _ in range(N):
    opisanie = input().split()
    for word in opisanie:
        if word == "зайка":
            zayka_count += 1

print(zayka_count)