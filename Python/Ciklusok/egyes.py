n = int(input("n: "))

print(1)
for i in range(2, n+1):
    print(i, end=" ")
    for j in range(i-2):
        print(1, end=" ")
    print(i)