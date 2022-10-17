n = int(input("n: "))
p = int(input("p: "))

k = 0 #karakterisztika

while n % p == 0:
    k += 1
    n //= p

m = n #mantissza

print(str(p) + "^" + str(k) + " * " + str(m))