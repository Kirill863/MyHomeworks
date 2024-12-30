L = int(input())
N = int(input())
zagolovki = []

for _ in range(N):
    zagolovok = input()
    zagolovki.append(zagolovok)

for zagolovok in zagolovki:
    if len(zagolovok) > L:
        zagolovok = zagolovok[:L - 3] + "..."
    print(zagolovok)

