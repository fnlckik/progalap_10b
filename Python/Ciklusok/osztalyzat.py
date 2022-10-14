n = int(input("Osztalyzat (1<=n<=5): "))
#jo = 1 <= n and n <= 5
jo = 1 <= n <= 5
while not jo:
    print("Nem jo: 1<=n<=5")
    n = int(input("Osztalyzat: "))
    #jo = 1 <= n and n <= 5
    jo = 1 <= n <= 5