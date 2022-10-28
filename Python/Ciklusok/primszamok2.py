#Be: m (egesz)
#Ki: 1-tol m-ig a primszamok

#Pl.: m = 23 -> 2 3 5 7 11 13 17 19 23

#2-tol m-ig minden szamrol eldondjuk, hogy prim-e
m = int(input("m: "))
print(2, end=" ")
j = 3
while j <= m:

    #Eldontjuk, hogy j szam prim-e
    n = j
    primE = True

    i = 2
    while i < n and primE:
        if n % i == 0:
            primE = False
        i += 1

    #Ha prim, akkor kiirjuk
    if primE:
        print(j, end=" ")

    j += 2
