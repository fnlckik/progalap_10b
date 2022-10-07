ev = int(input("2000 utani ev: "))

if ev >= 2000:
    if ev % 4 == 0:
        print("Szokoev")
    else:
        print("Nem szokoev")
else:
    print("Buta vagy! 2000 utani ev kellene!")