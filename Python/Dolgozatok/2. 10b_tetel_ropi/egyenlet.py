n = int(input())
szamok = []
for i in range(n):
    szam = int(input())
    szamok.append(szam)

maxi = 0
#maxe = szamok[0]
for i in range(1, n):
    if szamok[i] > szamok[maxi]:
        maxi = i
        #maxe = szamok[i]
maxe = szamok[maxi]

print(maxi+1, maxe)