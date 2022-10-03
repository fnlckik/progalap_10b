#Beolvasas
bal = input("1. sorszam: ") #3
jobb = input("2. sorszam: ") #7

#Feldolgozas
'''
seged = bal #seged == 3; bal == 3
bal = jobb #bal == 7; jobb == 7
jobb = seged #jobb == 3; seged == 3
'''
bal, jobb = jobb, bal

#Kiiras
print(bal, jobb)
