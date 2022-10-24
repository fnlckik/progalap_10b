a = float(input("1. pont: "))
b = float(input("2. pont: "))
c = float(input("3. pont: "))
atlag = (a + b + c) / 3
jo = atlag >= 80

#while atlag < 80:
while not jo:
    print("Tanulni kéne! Újraírjuk!")
    a = float(input("1. pont: "))
    b = float(input("2. pont: "))
    c = float(input("3. pont: "))
    atlag = (a + b + c) / 3
    jo = atlag >= 80

print("Átlag: ", round(atlag, 2), "%", sep="")