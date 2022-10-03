#Beolvas
ketjegyu = int(input("Szam: ")) #75

#Feldolgoz
'''
t = ketjegyu // 10 #7
e = ketjegyu % 10 #5
eredmeny = e * 10 + t #57
'''
eredmeny = (ketjegyu-(ketjegyu//10 * 10)) * 10 + (ketjegyu // 10) 

#Kiir
print("Eredmeny:", eredmeny)
