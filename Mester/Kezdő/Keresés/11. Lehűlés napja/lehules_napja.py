#Beolvas
n = int(input())
minHo = []
maxHo = []
for i in range(n):
    sor = input().split()
    minHo.append(int(sor[0]))
    maxHo.append(int(sor[1]))
#print(minHo, maxHo)

#Kereses
i = 1
while i < n and not(maxHo[i] < minHo[i-1]):
    i += 1
if i < n:
    sorszam = i + 1
else:
    sorszam = -1

#Kiiras
print(sorszam)