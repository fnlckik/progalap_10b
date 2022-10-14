nev1 = input("Nev1: ")
nev2 = input("Nev2: ")
pont1 = int(input("Pont1: "))
pont2 = int(input("Pont2: "))

if pont1 > pont2:
    print(nev1, "nyert")
elif pont2 > pont1:
    print(nev2, "nyert")
else:
    print("Döntetlen!")