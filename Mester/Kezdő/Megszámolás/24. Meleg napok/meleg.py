#Beolvasas
be = list(map(int, input().split())) #[7, 30]
n = be[0] #7
k = be[1] #30
homersekletek = []
for i in range(n):
    h = int(input())
    homersekletek.append(h)
    #print(homersekletek)

#Feldolgozas (megszamolas)
db = 0
for i in range(n):
    if homersekletek[i] > k:
        db += 1

#Kiiras
print(db)