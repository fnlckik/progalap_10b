#Be: n (egesz)
#Ki: primszam-e? (Primszam / Nem primszam)

n = int(input("n: "))

primE = True

i = 2
while i < n and primE:
    if n % i == 0:
        primE = False
        #print(i)
        #print("Nem primszam!")
    i += 1

#print(primE)
if primE:
    print("Prímszám!")
else:
    print("Nem prímszám! Legkisebb osztoja:", i-1)