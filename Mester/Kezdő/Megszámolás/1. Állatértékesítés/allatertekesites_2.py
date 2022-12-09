n = int(input())
bevetelek = [0]
for i in range(n):
    bevetel = int(input())
    bevetelek.append(bevetel)
#print(bevetelek)

db = 0
for i in range(1, n+1):
    if bevetelek[i] > bevetelek[i-1]:
        db += 1

print(db)