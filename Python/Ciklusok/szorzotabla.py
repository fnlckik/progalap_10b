n = int(input("n: "))

#sorok kiiratasa
for i in range(1, n+1):
    #egy sor kiirasa
    for j in range(1, n+1):
        print(i * j, end=" ")
    print()