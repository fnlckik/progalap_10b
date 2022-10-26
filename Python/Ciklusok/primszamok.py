#Be: m (egesz)
#Ki: 1-tol m-ig a primszamok

#Pl.: m = 23 -> 2 3 5 7 11 13 17 19 23

m = int(input("m: "))
j = 2
while j <= m:

    n = j
    primE = True

    i = 2
    while i < n and primE:
        if n % i == 0:
            primE = False
        i += 1

    if primE:
        print(j, end=" ")

    j += 1
