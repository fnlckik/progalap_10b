#Beolvasas
ido = int(input("Masodperc: ")) #3723

#Feldolgozas
ora = ido // 3600 #1
maradek = ido % 3600 #123
perc = maradek // 60 #2
masodperc = maradek % 60 #3

#Kiiras
print("Eltelt ido:", ora, "ora", perc, "perc", masodperc, "masodperc")
