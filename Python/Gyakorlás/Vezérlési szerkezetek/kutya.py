kor = float(input("Kutya életkora emberi évben: "))

if kor >= 2:
    kutya = 2*10.5 + 4*(kor-2)
else:
    kutya = kor * 10.5

print("Kutya életkora kutya években:", round(kutya, 2))