n = int(input("n: "))

for i in range(500, 601):
    if i % n == 0:
        print("#", end=" ")
    else:
        print(i, end=" ")