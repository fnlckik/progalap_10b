n = int(input("n: "))
jo = (n % 10) % 3 == 0
while not jo:
    print("Utolso szamjegy legyen oszthato 3-mal!")
    n = int(input("n: "))
    jo = (n % 10) % 3 == 0