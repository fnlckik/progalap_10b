#Beolvasas
#n, k = list(map(int, input().split()))
sor = input().split()
n = int(sor[0])
k = int(sor[1])
arak = []
for i in range(n):
    ar = int(input())
    arak.append(ar)
    #arak.append(int(input()))

#Kereses
i = 0
while i < n and not(arak[i] < k):
    i += 1
if i < n:
    sorszam = i + 1
else:
    sorszam = -1

#Kiiras
print(sorszam)