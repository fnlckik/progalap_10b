a = float(input("alap: "))
n = int(input("kitevo: "))

hatvany = 1
for i in range(n):
    hatvany *= a

print("hatvany:", hatvany)