lista = [7, -3, 10, 27, 92, 23, 18, 73, -21, 12, -9, 30, -4, 5]

n = len(lista)
elso = lista[0]
db = 0
for i in range(n):
    if elso < lista[i] and lista[i] % 2 == 1:
        db += 1

print(db)