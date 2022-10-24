a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

db = 0
for i in range(a, b+1):
    if i % c == 0:
        db += 1

print(db)