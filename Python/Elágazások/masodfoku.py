a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b**2 - 4*a*c

if D > 0:
    print("Ket valos megoldas.")
elif D == 0:
    print("Egy valos megoldas.")
else:
    print("Nincs valos megoldas.")