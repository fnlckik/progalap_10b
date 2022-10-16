#Beolvasas
a = int(input("a: "))
b = int(input("b: "))

jo = a != b
while not jo:
    print("Nem lehetnek egyenlok!")
    a = int(input("a: "))
    b = int(input("b: "))
    jo = a != b

#Feldolgozas
if a > b:
    a, b = b, a

szorzat = 1
i = a
while i <= b:
    if i % 2 == 1:
        szorzat *= i
    i += 1

#Kiiras
print("A paratlanok szorzata " + str(a) + "-tol " + str(b) + "-ig:", szorzat)