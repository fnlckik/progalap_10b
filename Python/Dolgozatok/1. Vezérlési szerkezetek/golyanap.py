osztaly = input("Osztály neve: ")
pontszam = int(input("Pontszám: "))

hianyzik = 60 - pontszam

if osztaly == "a":
    print("Nyertek a közgazdászok! Csak", hianyzik, "pontot vesztettek!")
elif osztaly == "b":
    print("Győztek a gazdinfósok! Csak", hianyzik, "pontot vesztettek!")
else:
    print("Infósok a legjobbak! Csak", hianyzik, "pontot vesztettek!")