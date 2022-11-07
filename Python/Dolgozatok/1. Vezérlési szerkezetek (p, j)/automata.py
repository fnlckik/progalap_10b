ar = 1670

be = int(input("Add meg az osszeget: "))

if be < ar:
    print("Sikertelen vásárlás! Hiányzik ", ar - be, "Ft.", sep="")
elif be == ar:
    print("Sikeres vásárlás! Nincs visszajáró!")
else:
    print("Sikeres vásárlás! Visszajáró: ", be - ar, "Ft.", sep="")