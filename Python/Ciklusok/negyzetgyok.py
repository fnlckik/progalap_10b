x = float(input("x: ")) #Mennyi a gyok(2)?

#Kezdeti intervallum: [0; x]
bal = 0
jobb = x
#print(bal, jobb)

for i in range(50):
    felezo = (bal + jobb) / 2
    if felezo*felezo < x: 
        #jobban megyunk tovabb
        bal = felezo
    else:
        #balban megyunk tovabb
        jobb = felezo
    #print(bal, jobb)

print(x, "negyzetgyoke:", round(felezo, 4))