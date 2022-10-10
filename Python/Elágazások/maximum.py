a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a >= b and a >= c:
    print("max:", a)
elif b >= c and b >= a:
    print("max:", b)
else:
    print("max:", c)