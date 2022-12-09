n = int(input())
bevetelek = []
for i in range(n):
    bevetel = int(input())
    bevetelek.append(bevetel)

'''
if bevetelek[0] == 0:
    db = 0
else:
    db = 1
'''
db = 0
for i in range(1, n):
    if bevetelek[i] > bevetelek[i-1]:
        db += 1
if bevetelek[0] > 0:
    db += 1

print(db)