n = int(input("n: "))

for i in range(2, n):
    if n % i == 0:
        print("nem prím")
        exit()

print("prím")