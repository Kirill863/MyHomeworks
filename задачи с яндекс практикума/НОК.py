a = int(input())
b = int(input())

a_1 = a
b_1 = b

while a != b:
    if a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    else:
        nod = a, b
nod = a

nok = (a_1 * b_1) // nod
print(nok)