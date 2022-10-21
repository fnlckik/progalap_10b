n = int(input("n: "))

szam = 0
for i in range(1, n+1):
    for j in range(i):
        szam += 1
        print(szam, end=" ")
    print()