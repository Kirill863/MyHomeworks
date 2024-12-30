
L = int(input())
N = int(input())
zagolovki = []
for _ in range(N):
    zagolovk = input()
    zagolovki.append(zagolovk)

for zagolovk in zagolovki:
    if len(zagolovk) > L:
        zagolovk = zagolovk[:L-3] + "..."
    print(zagolovk)

