szamok = [5, 7, -3, 4, 2]
n = len(szamok)

#Osszegzes (osszeg)
osszeg = 0
for i in range(n):
    osszeg = osszeg + szamok[i]

#Osszegzes (negyzetosszeg)
negyzetOsszeg = 0
for i in range(n):
    negyzetOsszeg = negyzetOsszeg + szamok[i] ** 2

#Osszegzes (szorzat)
szorzat = 1
for i in range(n):
    szorzat = szorzat * szamok[i]

#K: 5-nel kisebb elemek osszege?
kisosszeg = 0
for i in range(n):
    if szamok[i] < 5:
        kisosszeg = kisosszeg + szamok[i]

print("Osszeg:", osszeg)
print("Negyzetosszeg:", negyzetOsszeg)
print("Szorzat:", szorzat)
print("5-nel kisebbek osszege:", kisosszeg)