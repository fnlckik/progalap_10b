n = int(input())
varosok = []
erkezesek = []
indulasok = []
for i in range(n):
    sor = input().split()
    varosok.append(sor[0])
    erkezesek.append(int(sor[1]))
    indulasok.append(int(sor[2]))
#print(varosok, erkezesek, indulasok, sep="\n")

i = 0
#i < n 
while i < n and not(varosok[i] == "Szekesfehervar" and erkezesek[i] == -1):
    i += 1
if i < n:
    ki = indulasok[i]
else:
    ki = -1

print(ki)