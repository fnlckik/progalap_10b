n = int(input())
hosszusagok = []
szelessegek = []
for i in range(n):
    sor = input().split()
    sz = int(sor[0])
    h = int(sor[1])
    hosszusagok.append(h)
    szelessegek.append(sz)
# print(hosszusagok, szelessegek)

osszeg = 0
for i in range(n):
    aktTer = szelessegek[i] * hosszusagok[i]
    osszeg += aktTer
    #osszeg = osszeg + aktTer

'''
osszeg = 0
i = 0
while i < n:
    aktTer = szelessegek[i] * hosszusagok[i]
    osszeg += aktTer
    i += 1
'''

print(osszeg)