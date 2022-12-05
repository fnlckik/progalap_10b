#Beolvasas
be = input().split()
n = int(be[0])
mkorl = int(be[1])
arkorl = int(be[2])
arak = []
meretek = []
for i in range(n):
    be = input().split()
    ar = int(be[0])
    arak.append(ar)
    meret = int(be[1])
    meretek.append(meret)

#Kereses
i = 0
#(mkorl >= meretek[i] or arkorl >= arak[i])
while i < n and not(mkorl < meretek[i] and arkorl < arak[i]):
    i += 1
if i < n:
    ki = i + 1
else:
    ki = 0

#Kiiras
print(ki)