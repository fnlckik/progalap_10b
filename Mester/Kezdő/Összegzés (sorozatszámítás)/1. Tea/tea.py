#Beolvasas
n = int(input())
fajtak = []
mennyisegek = []
for i in range(n):
    #fajta beolvas
    #fajtak.append(input())
    fajta = input()
    fajtak.append(fajta)
    #menny beolvas
    mennyiseg = int(input())
    mennyisegek.append(mennyiseg)
#print(fajtak, mennyisegek)

'''
#Feldolgozas (osszegzes)
s = 0
elsoFajta = fajtak[0] #Lipton
for i in range(n):
    if fajtak[i] == elsoFajta:
        s += mennyisegek[i]
'''

s = mennyisegek[0]
for i in range(1, n):
    if fajtak[i] == fajtak[0]:
        s += mennyisegek[i]

#Kiiras
print(s)