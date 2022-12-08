#Beolvasas
n = int(input())
korok = []
fizetesek = []
for i in range(n):
    sor = list(map(int, input().split()))
    korok.append(sor[0])
    fizetesek.append(sor[1])
#print(korok, fizetesek)

#Maximum
maxi = 0
for i in range(1, n):
    if korok[i] > korok[maxi]:
        maxi = i

#Kiiras
print(fizetesek[maxi])