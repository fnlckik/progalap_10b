n = int(input("n: "))
jo = (n % 10) % 3 == 0
while not jo:
    n = int(input("n: "))
    jo = (n % 10) % 3 == 0