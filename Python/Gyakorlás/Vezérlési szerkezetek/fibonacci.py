n = int(input("n: "))

a = 1
b = 1

print(a, b, end=" ")
for i in range(n-2):
    fib = a + b
    a = b
    b = fib
    print(fib, end=" ")