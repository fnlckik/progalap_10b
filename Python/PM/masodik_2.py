a = 6
b = 15
c = int(input())

if a % c == 0 and b % c == 0:
    print(a, b)
elif a % c == 0:
    print(a)
elif b % c == 0:
    print(b)
else:
    print(c)
print("Macska")