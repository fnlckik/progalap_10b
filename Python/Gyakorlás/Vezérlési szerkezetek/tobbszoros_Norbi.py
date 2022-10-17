n = int(input("n: "))

for i in range(999, 0, -1):
    if i % n == 0:
        print(i, end=" ")
