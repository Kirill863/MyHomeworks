n = int(input())

for i in range(n):
    for j in range(n):
        print(min(i + 1, j + 1, n - i, n - j), end=' ')
    print()

# Верное решение #894401050
# Python 3.10
def make_dartboard(n):
    dartboard = [[1] * n for _ in range(n)]
    step = 1
    while step < n - step:
        for row in range(step, n - step):
            for column in range(step, n - step):
                dartboard[row][column] += 1
        step += 1
    return dartboard

dartboard = make_dartboard(int(input()))

for line in dartboard:
    print(*line)