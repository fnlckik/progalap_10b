from random import *

egy = 0
ketto = 0
harom = 0

for i in range(500000):
    #veletlen eloallitasa
    #szam = round(random() * 2) + 1 #ROSSZ
    #szam = int(random() * 3) + 1 #HELYES
    szam = randint(1, 3)
    print(szam, end=" ")
    if szam == 1:
        egy += 1
    elif szam == 2:
        ketto += 1
    else:
        harom += 1

print()
print("Egyesek:", egy)
print("Kettesek:", ketto)
print("Harmasok:", harom)