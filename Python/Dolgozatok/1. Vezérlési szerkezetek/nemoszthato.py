n = int(input("n: "))

for i in range(1, 101):
    #if i % n != 0:
    if not i % n == 0:
        print(i, end=" ")