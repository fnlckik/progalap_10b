a = int(input("a: "))
b = int(input("b: "))

if a > 5 and b > 5:
    print("Mindkét osztályban halasztani kell!")
elif a > 5: #and b <= 5
    print("A-ban halasztani kell!")
elif b > 5: #and a <= 5
    print("B-ben halasztani kell!")
else:
    print("Sehol sem kell halasztani!")
