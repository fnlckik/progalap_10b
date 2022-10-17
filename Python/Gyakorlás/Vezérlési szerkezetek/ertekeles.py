pontszam = int(input("Pontszam: "))

if pontszam < 0 or pontszam > 100:
    print("Nem jo!")
    exit()

# 0 <= pontszam <= 42
if pontszam <= 42:
    print("elégtelen")
elif pontszam <= 57:
    print("elégséges")
elif pontszam <= 72:
    print("közepes")
elif pontszam <= 87:
    print("jó")
else:
    print("jeles")