n = int(input("n: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print("b"*i, end="")
    else:
        print("a"*i, end="")