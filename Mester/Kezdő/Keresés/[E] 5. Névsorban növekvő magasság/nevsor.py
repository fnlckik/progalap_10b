#Beolvasas
n = int(input())
nevek = []
magassagok = []
for i in range(n):
    sor = input().split()
    nevek.append(sor[0])
    magassagok.append(int(sor[1]))
#print(nevek, magassagok)

#Eldontes
i = 1
while i < n and not(magassagok[i] < magassagok[i-1]):
    i += 1
if i < n:
    print("NEM")
else:
    print("IGEN")

#Hanyan magasabbak az atlagnal?



#Add meg az elso embert, akinek a neve 5 karakternel hosszabb!
#Ha nincs ilyen, akkor azt, hogy "Nincs ilyen!"


