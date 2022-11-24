#Beolvasas
n = int(input())
k = []
p = []
for i in range(n):
    #sor = list(map(int, input().split())) #[42, 15]
    be = input() #"42 15"
    lista = be.split() #["42", "15"]
    sor = list(map(int, lista)) #[42, 15]
    k.append(sor[0])
    p.append(sor[1])
print(k, p, sep="\n")

#Feldolgozas (megszamolas)
db = 0
for i in range(n):
    if k[i] < p[i]:
        db += 1

#Kiiras
print(db)