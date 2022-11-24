#Beolvasas
#n, p, q beolvasas
be = input()
lista = be.split()
szamok = list(map(int, lista))
n = szamok[0] #6
p = szamok[1] #200
q = szamok[2] #220

#tejarak beolvasasa
tejarak = []
for i in range(n):
    ar = int(input())
    tejarak.append(ar)
#print(tejarak)

#Feldolgozas (megszamolas tetel)
db = 0
for i in range(n):
    if p <= tejarak[i] and tejarak[i] <= q:
        db += 1

#Kiiras
print(db)