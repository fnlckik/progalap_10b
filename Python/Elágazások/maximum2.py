#Beolvasas
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

#Feldolgozas
maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

#Kiiras
print("max:", maximum)