n = int(input("n: "))
összeg = 0

for i in range(n+1):
    if i % 2 == 1:
        összeg += i

print(összeg)
