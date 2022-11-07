n = int(input("n: "))

fakt = 1
for i in range(n, 1, -2):
    #print(i, end=" ")
    fakt = fakt * i

#print()
print("n!! =", fakt)