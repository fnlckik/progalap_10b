#Beolvasas
n = int(input())
idok = []
for i in range(n):
    ido = int(input())
    idok.append(ido)
    #idok.append(int(input()))

#Kereses
i = 1
while i < n and not(idok[i] < idok[i-1]):
    i += 1
if i < n:
    sorszam = i + 1
else:
    sorszam = -1

print(sorszam)