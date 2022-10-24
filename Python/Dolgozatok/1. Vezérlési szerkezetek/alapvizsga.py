pontszam = int(input("Pontszám: "))
osszpont = int(input("Összpont: "))
szazalek = pontszam / osszpont * 100

while szazalek < 40:
    print("Fuss neki újra!")
    pontszam = int(input("Pontszám: "))
    osszpont = int(input("Összpont: "))
    szazalek = pontszam / osszpont * 100

print("Végre sikerült! Az eredményed ", round(szazalek, 2), "%", sep="")