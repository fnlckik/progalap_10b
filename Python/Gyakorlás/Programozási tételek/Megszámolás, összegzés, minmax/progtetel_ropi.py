#Adatok
x = [7, 9, 12, 3, -5, -2, 8, -5, 18, -1]
n = len(x)

#1. Parosak szama? 4
dbParos = 0
for i in range(n):
    if x[i] % 2 == 0:
        dbParos += 1
print("Parosak szama:", dbParos)

#2. Legnagyobb elem erteke? 18
maxe = x[0]
for i in range(1, n):
    if x[i] > maxe:
        maxe = x[i]
print("Legnagyobb elem:", maxe)

maxi = 0
for i in range(1, n):
    if x[i] > x[maxi]:
        maxi = i
print("Legnagyobb elem helye:", maxi+1)
print("Legnagyobb elem erteke:", x[maxi])

#3. Negativak szorzata? 50
szorzat = 1
for i in range(n):
    if x[i] < 0:
        szorzat *= x[i]
print("Negativak szorzata:", szorzat)

#4. Legkisebb elem hol van (utolso hely)? 8
mini = 0 #mine = x[0]
for i in range(1, n):
    if x[i] <= x[mini]:
        mini = i
print("Legkisebb elem indexe:", mini+1)

#5. Atlag? 4.4
s = 0
for i in range(n):
    s += x[i]
atlag = s / n
print("Atlag:", atlag)
