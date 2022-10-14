x = float(input("x: "))
y = float(input("y: "))

if x == 0 or y == 0:
    print("Az egyik tengelyre esik a pont.")

if x > 0 and y > 0:
    print("1. siknegyed")
elif x < 0 and y > 0:
    print("2. siknegyed")
elif x < 0 and y < 0:
    print("3. siknegyed")
else:
    print("4. siknegyed")