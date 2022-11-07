#Beolvasas
a = int(input("a: "))

#Feldolgozas
akt = a
parosDb = 0
for i in range(40):
    if akt % 2 == 0:
        parosDb += 1
    print(akt, end=" ")
    akt = (akt * 3) % 7
szazalek = parosDb/40 * 100

#Kiiras
print()
print("A tagok ", round(szazalek, 2), "%-a páros.", sep="")