a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and b + c > a and c + a > b:
    print("Szerkesztheto!")
else:
    print("Nem szerkesztheto!")