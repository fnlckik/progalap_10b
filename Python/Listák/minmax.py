lista = [4, -7, 2, 3, 1, 4, -5]
n = len(lista)

#Min ertek
mine = lista[0] #Minimalis ertek
for i in range(1, n):
    if lista[i] < mine:
        mine = lista[i]
print("Minimalis ertek:", mine)

#Max ertek
maxe = lista[0] #Maximalis ertek
for i in range(1, n):
    if lista[i] > maxe:
        maxe = lista[i]
print("Maximalis ertek:", maxe)

#Max hely (elso)
maxi = 0 #Maximalis erteku elem indexe
for i in range(1, n):
    if lista[i] > lista[maxi]:
        maxi = i
print("Maximum hely:", maxi+1)

#Max hely (utolso)
maxi = 0 #Maximalis erteku elem indexe
for i in range(1, n):
    if lista[i] >= lista[maxi]:
        maxi = i
print("Maximum hely:", maxi+1)