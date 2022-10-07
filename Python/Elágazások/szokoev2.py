ev = int(input("2000 utani ev: "))

if ev >= 2000 and ev % 4 == 0:
    print("Szokoev")
elif ev >= 2000: #and ev % 4 != 0
    print("Nem szokoev")
else:
    print("Buta vagy! 2000 utani ev kellene!")