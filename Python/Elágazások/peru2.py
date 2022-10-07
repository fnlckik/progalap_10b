osztalyzat = int(input("Osztalyzat: "))

if osztalyzat < 1 or osztalyzat > 20:
    print("Hibas! (1<=osztalyzat<=20 kellene)")
    exit()

if osztalyzat <= 10:
    print("Bukott!")
else:
    print("Atment!")

print("Program vege!")