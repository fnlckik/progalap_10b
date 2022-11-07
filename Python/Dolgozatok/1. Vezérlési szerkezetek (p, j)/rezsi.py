sorsz = 1
hom = float(input("1. nap: "))

while hom >= 18:
    sorsz += 1
    print(sorsz, end="")
    hom = float(input(". nap: "))

print("Ami sok az sok! Ez viszont kevés! Most már ideje fűteni!")