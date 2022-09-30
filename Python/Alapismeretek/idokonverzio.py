#Beolvasas
o = int(input("Ora: "))
p = int(input("Perc: "))
mp = int(input("Masodperc: "))

#Feldolgozas
ido = o * 60 * 60 + p * 60 + mp
# ido = o * 60 ** 2 + p * 60 + mp
# ido = o * 3600 + p * 60 + mp

#Kiiras
print("Mostani ido:", ido)