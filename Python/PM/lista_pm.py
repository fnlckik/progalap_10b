szamok = [11, 2, 7, 3]
print(szamok[2]) #7
szamok.append(18) #szamok == [11, 2, 7, 3, 18]
print(len(szamok)) #5
u = szamok.pop() #szamok == [11, 2, 7, 3], u == 18
szamok.clear() #szamok == []
szamok.append(7) #szamok == [7]
szamok.append(3) #szamok == [7, 3]
print(u + szamok[1]) # 18 + 3 == 21

#7
#5
#21