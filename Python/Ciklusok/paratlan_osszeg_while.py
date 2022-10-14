n = int(input("n: "))

osszeg = 0
i = 1
while i <= n:
    osszeg += i
    i += 2

print("Paratlanok osszege:", osszeg)